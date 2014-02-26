import time
'''
class AbstractAgent(object):
    def __init__(self,queue_num,process_time):
        self.queue_num = queue_num
        self.process_time = process_time
        
      
class License_agent(AbstractAgent):
    
    
    def check(self, customer):
        if customer.passport == None or customer.drivers_license == None or emirates_id == None:
            ##put into fail queue/array
            ## return fail
        if 
    def send_printer(self):
        
class Eye_tester(AbstractAgent):
    
    
class Translator(AbstractAgent):
'''   
    
class printer():
    def __init__(self):
        self.state = 'idle'
    
    def isIdle(self):
        if self.state =="idle":
            return True
        else:
            return False
    
    def change_state(self): 
        if self.state == "idle":
            self.state = "busy"
        else:
            self.state = "idle"
    
    def start_printing(self,random_time, customer, queue_name):
        time.sleep(random_time)
        ##Put it into successful queue! 
        ##queue_name.put(customer)
        self.change_state()
        
        