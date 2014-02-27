from Queue import Queue
import random
from agents import *
import assignment1
from datetime import date
import pickle
import threading

## pickle example favorite_color = pickle.load( open( "save.p", "rb" ) )
## Number of each agent and printer(testing)
printer_num = 5
license_agent = 5
translation_agent = 5
eyetest_agent = 5

print threading.active_count()
for i in range(5):
    a = License_Agent().run()
    
for i in range(5):
    a = Eye_test_Agent().run()
    
for i in range(5):
    a = Translate_Agent().run()
    

    


data = pickle.load(open("customer.dat","rb"))
receptionist = reception("smart")
for i in data:
    receptionist.place(i)

while threading.active_count()>1:
    pass

print success_list

print "yes"
