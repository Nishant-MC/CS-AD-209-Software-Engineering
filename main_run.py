from Queue import Queue
import random
from agents import *
import assignment1
from datetime import date
import pickle
import threading
import queue
from operator import itemgetter
## pickle example favorite_color = pickle.load( open( "save.p", "rb" ) )
## Number of each agent and printer(testing)
printer_num = 5
license_agent = 5
translation_agent = 5
eyetest_agent = 5
## this function watches for an idle printer and pushs printing job to the idle one
def printer_checker(customer_size):
    while True:
        if not print_q.Q.empty():
            for i in printers:
                if i.isIdle():
                    i.start_printing(print_q.dequeue())
                    break

        if (print_q.Q.empty() and len(success_list)+len(fail_list)==customer_size
            and eye_test_q.Q.empty() and license_q.Q.empty()
             and translation_q.Q.empty() and len(customer_list)==0):
            #print "Done PPPPPPPPPPP"
            break
printers = [printer() for x in range(printer_num)]

##Test Data##
data = pickle.load(open("customer.dat","rb"))

def run(data):
    sorted(data,key=itemgetter(0))
    data = [cus for(arrival,cus) in data]
    customer_size = len(data)

    for i in range(license_agent):
        t1 = threading.Thread(target=License_Agent().run,args=(customer_size,))
        t1.start()
        
    for i in range(eyetest_agent):
        t1 = threading.Thread(target=Eye_test_Agent().run,args=(customer_size,))
        t1.start()
        
    for i in range(translation_agent):
        t1 = threading.Thread(target=Translate_Agent().run,args=(customer_size,))
        t1.start()

    # Initialize Print_checker    
    t1 = threading.Thread(target=printer_checker, args=(customer_size,))
    t1.start()
    
    receptionist = reception("smart")
    
    for i in data:
        receptionist.place(i)
    
    while True:
        if (print_q.Q.empty() and len(success_list)+len(fail_list)==customer_size
             and eye_test_q.Q.empty() and license_q.Q.empty() and
              translation_q.Q.empty() and len(customer_list)==0):
            break
    #print success_list
    
    #print len(success_list)
    #print len(fail_list)
    return success_list

a = run(data)
