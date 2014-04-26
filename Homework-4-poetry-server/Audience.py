#!/bin/python
import os
import json
import logging

from twisted.internet import reactor, defer

from stompest.async import Stomp
from stompest.async.listener import SubscriptionListener
from stompest.config import StompConfig
from stompest.protocol import StompSpec


class Audience(object):

    QUEUE = '/queue/poems'
    ERROR_QUEUE = '/queue/poems/error'

    def __init__(self, config=None):
        if config is None:
            address = os.getenv('ACTIVEMQ_PORT_61616_TCP', 'tcp://localhost:61616')
            config = StompConfig(address)
        self.config = config
        self.POETRY = {}

    @defer.inlineCallbacks
    def run(self):
        client = yield Stomp(self.config).connect()
        headers = {
            # client-individual mode is necessary for concurrent processing
            # (requires ActiveMQ >= 5.2)
            StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL,
            # the maximal number of messages the broker will let you work on at the same time
            'activemq.prefetchSize': '100',
        }
        client.subscribe(self.QUEUE, headers, listener=SubscriptionListener(self.consume, errorDestination=self.ERROR_QUEUE))

    def getTitle(self, message):
        self.POETRY[message["name"]]["count"] = message["length"]

    def getLine(self, message):
        if (self.data["type"] != "title"):
            name = message["name"]
            self.POETRY[name]["length"].append(message)
        else:
            self.getTitle(data)

    def sitRep(self, name):
        poem = self.POETRY[name]
        if ("count" not in poem or poem["count"] > len(poem["length"])):
            print "I have %d lines of poetry from %s" % (len(poem["length"]), name)
        else:
            self.printPoem(poem)

    def printPoetry(self, poem):
        lines = sorted(poem["length"], key=lambda msg: msg['line'])
        print "This is from: %s" % poem["name"]
        for line in lines:
            print line["content"]

    def consumer(self, client, frame):
        data = json.loads(frame.body)
        name = data["name"]

        if name not in self.POETRY:
            self.POETRY[name] = {
                    "name": name,
                    "length": []
            }

        self.getLine(data)
        self.sitRep(name)

def main():
    Audience().run()
    reactor.run()

if __name__ == '__main__':
    main()
