import Queue

class queue():
    def __init__(self,queue_type):
        self.Q = Queue.Queue()
        self.ticket_count = -1
        self.process_count = -1
        self.next_ticket = 0
        self.queue_type = queue_type
    
    def add(self,item):
        self.ticket_count += 1
        self.Q.put([item,self.queue_type+str('{0:04}'.format(self.ticket_count%10000))])
        
    def pop(self):
        self.process_count +=1
        return self.Q.get()
        
    def peek(self):
        return (self.ticket_count%10000) - (self.process_count%10000) + 1
    
    