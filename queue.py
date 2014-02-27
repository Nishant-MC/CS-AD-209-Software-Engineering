import Queue

class queue():
    def __init__(self,queue_type):
        self.Q = Queue.Queue()
        self.ticket_count = -1
        self.process_count = -1
        self.queue_type = queue_type
    
    def enqueue(self,item):
        self.ticket_count += 1
        self.Q.put(item)
        
    def dequeue(self):
        self.process_count +=1
        return self.Q.get()
        
    def peek(self):
        return (self.ticket_count%10000) - (self.process_count%10000) + 1
    
## empty method from Queue class eg] initialized_queue_class.Q.empty()
    