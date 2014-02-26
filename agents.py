import time
from datetime import date

class AbstractAgent(object):
    def __init__(self):
        self.ticket_num = None
        self.process_time = None
        self.occupied = False

def Isconsistent(docu):
    first_name =set([x.first_name for x in docu if x is not None])
    last_name =set([x.last_name for x in docu if x is not None])
    nationality =set([x.nationality for x in docu if x is not None])
    gender =set([x.gender for x in docu if x is not None])
    DOB =set([x.date_of_birth for x in docu if x is not None])
    
    if len(set([len(first_name),len(last_name),len(nationality),\
                len(gender),len(DOB)])) == 1:
        return True
    else:
        print "Fail from consistency test"
        return False
    

class License_Agent(AbstractAgent):
    def __init__(self):
        super(License_agent,self).__init__()
    
    
    def check(self, customer):
        self.occupied = True
        if customer.passport == None or customer.drivers_license == None\
         or emirates_id == None or customer.passport.expiry_date<date.today() \
         or customer.emirates_id.expiry_date<date.today() or \
         customer.drivers_license.expiry_date<date.today():
            fail_q.put(customer)
            return False
        
        if Isconsistent([customer.passport, customer.drivers_license,\
                          customer.emirates_id, customer.eye_test, \
                          customer.drivers_license_translation]):
            pass
        else:
            fail_q.put(customer)
            return False
        
        return_condition = False 
        
        if customer.eye_test == None or customer.eye_test.expiry_date < date.today():
            eye_test_q.put(customer)
            return_condition = True
            
        if customer.drivers_license_translation == None:
            translation_q.put(customer)
            return_condition = True
        
        if return_condition == True:
            return False
        return True
    
    def process(self,customer,process_time):
        time.sleep(process_time)
        printer_q(customer)
        self.occupied = False            
                    
class Eye_test_Agent(AbstractAgent):
    def __init__(self):
        super(Eye_test_Agent,self).__init__()
    ##def check(self, process_time):
        
    
class Translate_Agent(AbstractAgent):
    def __init__(self):
        super(Translate_Agent,self).__init__()
      
    
class printer():
    def __init__(self):
        self.state = 'idle'
    
    def isIdle(self):
        if self.state =="idle":
            return True
        else:
            return False
    
    def change_state(self,customer): 
        if self.state == "idle":
            self.state = "busy"
            start
        else:
            self.state = "idle"
    
    def start_printing(self,customer):
        time.sleep(300) # takes 300 seconds to print
        success_q.put(customer)
        self.change_state()
        
        