import time
from Queue import Queue
from datetime import date
import assignment1

## Create queues 
global license_q
license_q = Queue()
global translation_q
translation_q = Queue()
global eye_test_q
eye_test_q = Queue()
global fail_q
fail_q = Queue()

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
        super(License_Agent,self).__init__()
    
    
    def check(self, customer):
        self.occupied = True
        if customer.passport == None or customer.drivers_license == None\
         or customer.emirates_id == None or customer.passport.expiry_date<date.today() \
         or customer.emirates_id.expiry_date<date.today() or \
         customer.drivers_license.expiry_date<date.today():
            fail_q.put(customer)
            print "point1"
            return False
        
        if Isconsistent([customer.passport, customer.drivers_license,\
                          customer.emirates_id, customer.eye_test, \
                          customer.drivers_license_translation]):
            pass
        else:
            fail_q.put(customer)
            print "point2"
            return False
        
        return_condition = False 
        
        if customer.eye_test == None or customer.eye_test.expiry_date < date.today():
            customer.eye_test = None ##Set it to None so that it issues new date
            eye_test_q.put(customer)
            return_condition = True
        
        if customer.drivers_license_translation == None:
            translation_q.put(customer)
            return_condition = True
        
        if return_condition == True:
            print "point3"
            return False
        return True
    
    def process(self,customer,process_time):
        time.sleep(process_time)
        printer_q(customer)
        self.occupied = False            
                    
class Eye_test_Agent(AbstractAgent):
    def __init__(self):
        super(Eye_test_Agent,self).__init__()
    
    def process(self,customer, process_time):
        if customer in busy_customers:
            eye_test_q.put(customer)
        else:                
            busy_customers.append(customer)
            customer.eye_test = assignment1.EyeTest(customer.first_name, customer.last_name,\
                                                    customer.nationality, customer.gender,\
                                                    customer.date_of_birth,None)
            time.sleep(process_time)
            busy_customers.remove(customer)
            ### Check if it is in the other queue if not, put into license queue!
    
class Translate_Agent(AbstractAgent):
    def __init__(self):
        super(Translate_Agent,self).__init__()
    
    def process(self,customer):
        if customer in busy_customers:
            translation_q.put(customer)
        else:
            busy_customers.append(customer)  
            customer.drivers_license_translation = assignment1.Drivers_License_Translation(customer.drivers_license)
            time.sleep(process_time)
            busy_customers.remove(customer)
            ### Check if it is in the other queue if not, put into license queue!
            
class printer():
    def __init__(self):
        self.busy = False
    
    def isIdle(self):
        if self.busy == False:
            return True
        else:
            return False
    
    def change_state(self,customer): 
        if self.busy == False:
            self.busy = True
            
        else:
            self.busy = False
    
    def start_printing(self,customer):
        time.sleep(300) # takes 300 seconds to print
        success_q.put(customer)
        self.change_state()
        
        