import assignment1
import random
import string
from datetime import date, timedelta
import pickle

def name_generator():
    name_length=random.randrange(4,8)
    name=''
    for i in range(name_length):
        name += random.choice(string.uppercase) 
    return name

def dateofbirth():
    base = date(1950,1,1)
    random_day = random.randrange(0,18251)
    return base + timedelta(days=random_day)

def expiry_date(minus):
    base = date.today()+timedelta(days=5)
    random_day = random.randrange(5,30)
    if minus:
        dates = [base+timedelta(days=random_day), base-timedelta(days=random_day)]
        return random.choice(dates)
    else:
        return base+timedelta(days=random_day)

def id_number():
    id=''
    for i in range(2):
        id += random.choice(string.uppercase) 
    for i in range(4):
        id += str(random.randrange(0,10))
    return id
 
customer_num = 30
customers=[]
for i in range(customer_num):
    first_name = name_generator()
    last_name = name_generator()
    nationality = random.choice(["United Sates","United Kingdom","Australia"])
    gender = random.choice(["M","F"])
    DOB = dateofbirth()
    UAE_ID = assignment1.Emirates_ID(first_name,last_name,nationality,gender,DOB,expiry_date(False),id_number())
    DL = assignment1.Drivers_License(first_name,last_name,nationality,gender,DOB,expiry_date(False))
    passport=assignment1.Passport(first_name,last_name,nationality,gender,DOB,expiry_date(False))
    eye= assignment1.EyeTest(first_name,last_name,nationality,gender,DOB,expiry_date(True))
    DLT = random.choice([None,assignment1.Drivers_License_Translation(DL)])
    #print "\t".join([first_name,last_name,nationality,gender])+'\n'
    customers.append((random.randrange(0,1000),assignment1.Customer(UAE_ID,DL,passport,eye,DLT)))

pickle.dump(customers, open("customer.dat","wb"))

    
    
    