#!C:\Python27\pythonw.exe
import json
import logging
import optparse

from twisted.internet import defer, reactor
from stompest.config import StompConfig
from stompest.async import Stomp
from stompest.async.listener import ReceiptListener

def parse_args():
    usage = """
usage: %prog poetry-file
python Poet.py <poem.txt>
            """
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('Only one poem at a time please!')

    poem = args[0]

    if os.path.exists(args[0]) == False:
        parser.error('%s does not exist!' % poetry_file)

    return options, poem


class Poet(object):

    QUEUE = '/queue/poems'

    def __init__(self, name, text, config=None):
        if config is None:
            address = os.getenv('ACTIVEMQ_PORT_61616_TCP', 'tcp://localhost:61616')
            print "%s will receive a line of poetry." % address
            config = StompConfig(address)
        self.config = config
        self.name = name
        self.text = text.split('\n')

    @defer.inlineCallbacks

    def run(self):
        client = yield Stomp(self.config).connect()
        client.add(ReceiptListener(1.0))

        x = 0
        yield client.send(self.queue, json.dumps({'type': 'title', 'name': self.name, 'length': len(self.text)}), receipt='message-%d' % x)
        for line in self.text:
            x += 1
            yield client.send(self.QUEUE,
                              
                              json.dumps({'type': 'line',
                                          'name': self.name,
                                          'line': x,
                                          'content': line}),

                              receipt='message-%d' % x)

        client.disconnect(receipt='bye')
        yield client.disconnected
        reactor.stop()


def main():
    logging.basicConfig(level=logging.DEBUG)
    Poet().run()
    reactor.run()


if __name__ == '__main__':
    main()
