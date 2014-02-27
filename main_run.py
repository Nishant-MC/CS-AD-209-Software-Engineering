from Queue import Queue
import random  ##Usage: random.randrange()
from agents import *
import assignment1
from datetime import date

nationalities = ["United Sates","United Kingdom","Australia"]
'''
## Create queues 
global license_q
license_q = Queue()
global translation_q
translation_q = Queue()
global eye_test_q
eye_test_q = Queue()
global fail_q
fail_q = Queue()
'''
## Array to keep customers that are in process
busy_customers = []

## Number of each agent and printer(testing)
printer_num = 5
license_agent = 5
translation_agent = 5
eyetest_agent = 5

printers = [printer() for i in range(printer_num)]

first_name = 'Jin'
last_name = 'Bak' 
nationality = "Korean"
gender = "M"
dateofbirth = "1991/04/20"

id = assignment1.Emirates_ID(first_name,last_name,nationality,gender,'asdf',date(2014, 2, 28),'12345')
DL = assignment1.Drivers_License(first_name,last_name,nationality,gender,dateofbirth,date(2014, 2, 28))
Pass = assignment1.Passport(first_name,last_name,nationality,gender,dateofbirth,date(2014, 2, 28))
eye_test=None
DLT = None

person = assignment1.Customer(id,DL,Pass,eye_test,DLT)
license_q.put(person)
a = License_Agent().check(person)
print a
def run(data):
    pass