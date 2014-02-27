import time
from Queue import Queue
from datetime import date
import assignment1
import random
import threading

#Create queues
license_q = Queue()
translation_q = Queue()
eye_test_q = Queue()
fail_q = Queue()
print_q = Queue()

## Array to keep customers that are in process
busy_customers = []
eye_translation_list=[]

#Create list to store successful applications
success_list= []

## Function to check document consistency - Done!!
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

# Abstract Agent class for license_agent, eye_test_agent and translate_agent
class AbstractAgent(object):
    def __init__(self):
        self.ticket_num = None
        self.occupied = False
        
# License Agent -- Done!
class License_Agent(AbstractAgent):
    def __init__(self):
        super(License_Agent,self).__init__()
    
    def check(self, customer):
        self.occupied = True
        # First screening - fail or continue
        if customer.passport == None or customer.drivers_license == None\
         or customer.emirates_id == None or customer.passport.expiry_date<date.today() \
         or customer.emirates_id.expiry_date<date.today() or \
         customer.drivers_license.expiry_date<date.today():
            fail_q.put(customer)   # Fail case
            print "no docu"
            return False
        # Check if info on documents are consistent
        if Isconsistent([customer.passport, customer.drivers_license,\
                          customer.emirates_id, customer.eye_test]):
            pass
        else:
            fail_q.put(customer)   # Fail case
            print "goes to failq"
            return False
        
        return_condition = False 
        # Check if eye test document is expired or not available
        if customer.eye_test == None or customer.eye_test.expiry_date < date.today():
            print "Missing"
            customer.eye_test = None ##Set it to None so that it issues new date
            eye_test_q.put(customer)
            eye_translation_list.append(customer)
            return_condition = True
        
        # Check drivers license translation 
        if customer.drivers_license_translation == None:
            print "Missing"
            translation_q.put(customer)
            eye_translation_list.append(customer)
            return_condition = True
        
        if return_condition == True:
            return False
        ##Will return true or false, if true, process, else nothing
        return True
    
    def process(self,customer):
        print 'Processing'
        process_time = random.randrange(120,301)
        time.sleep(10) 
    
    def test(self):
        while True:
            if not license_q.empty():
                print "found"
                customer=license_q.get()
                if self.check(customer):
                    print "yyees"
                    self.process(customer)
                    success_list.append(customer)
                    print_q.put(customer)
            if license_q.empty() and translation_q.empty() and eye_test_q.empty() and len(success_list)!=0:
                return
            
              
    def run(self):
        t1 = threading.Thread(target=self.test,)
        t1.start()
                        
class Eye_test_Agent(AbstractAgent):
    def __init__(self):
        super(Eye_test_Agent,self).__init__()
    
    def process(self,customer):
        if customer in busy_customers:
            eye_test_q.put(customer)
        else:                
            busy_customers.append(customer)
            customer.eye_test = assignment1.EyeTest(customer.passport.first_name,
                                                    customer.passport.last_name,
                                                    customer.passport.nationality,
                                                    customer.passport.gender,
                                                    customer.passport.date_of_birth,None)
            process_time = random.randrange(120,301)
            time.sleep(5)
            busy_customers.remove(customer)
            eye_translation_list.remove(customer)
            if customer in eye_translation_list:
                pass
            else:
                license_q.put(customer)
            ### Check if it is in the other queue if not, put into license queue!
    def test(self):
        while True:
            if not eye_test_q.empty():
                customer=eye_test_q.get()
                self.process(customer)       
            if license_q.empty() and translation_q.empty() and eye_test_q.empty() and len(success_list)!=0:
                return
             
    def run(self):
        t1 = threading.Thread(target=self.test,)
        t1.start()
    
class Translate_Agent(AbstractAgent):
    def __init__(self):
        super(Translate_Agent,self).__init__()
    
    def process(self,customer):
        if customer in busy_customers:
            translation_q.put(customer)
        else:
            busy_customers.append(customer)  
            customer.drivers_license_translation = assignment1.Drivers_License_Translation(customer.drivers_license)
            process_time = random.randrange(120,301)
            time.sleep(process_time)
            busy_customers.remove(customer)
            eye_translation_list.remove(customer)
            if customer in eye_translation_list:
                pass
            else:
                license_q.put(customer)
            ### Check if it is in the other queue if not, put into license queue!
    def test(self):
        while True:
            if not translation_q.empty():
                customer=translation_q.get()
                self.process(customer)
            if license_q.empty() and translation_q.empty() and eye_test_q.empty() and len(success_list)!=0:
                return
    def run(self):
        t1 = threading.Thread(target=self.test,)
        t1.start()
                    
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
        success_list.put(assignment1.UAE_Drivers_License(customer))
        self.change_state()

## Reception class -- Done! 
class reception():
    def __init__(self,choice):
        self.choice = choice 
    
    def smart_reception(self,customer):
        if (customer.emirates_id==None or customer.drivers_license==None or customer.passport == None):
            fail_q.put(customer)
            return
            
        if (customer.emirates_id!=None and customer.drivers_license!=None and customer.passport != None\
            and customer.eye_test != None and customer.drivers_license_translation!=None):
            license_q.put(customer)
            return
        
        elif (customer.eye_test==None):
            eye_test_q.put(customer)
            return
        
        elif (customer.drivers_license==None):
            translation_q.put(customer)
            
            return
        else:
            fail_q.put(customer)
    
    def random_queue(self,customer):
        random_number = random.randrange(0,3)
        if random_number == 0:
            license_q.put(customer)
        elif random_number==1:
            eye_test_q.put(customer)
        elif random_number==2:
            translation_q.put(customer)
    
    def license_first(self,customer):
        license_q.put(customer)
    
    def place(self,customer):
        if self.choice=="smart":
            self.smart_reception(customer)
        elif self.choice=="randomly":
            self.random_queue(customer)
        elif self.choice=="license":
            self.license_first(customer)
        else:
            self.license_first(customer)           
            
            
            
            
            
        