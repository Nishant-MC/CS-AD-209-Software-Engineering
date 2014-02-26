# in a file called assignment1.py
# Python 2.7 version
# dates are Python datetime.date instances

class AbstractPrimaryDocument(object):
    def __init__(self, first_name, last_name, nationality, gender,
                 date_of_birth, expiry_date):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.expiry_date = expiry_date

class Emirates_ID(AbstractPrimaryDocument):
    def __init__(self, first_name, last_name, nationality, gender,
                 date_of_birth, expiry_date, id_number):
        super(Emirates_ID,self).__init__(first_name, last_name, nationality,
                                         gender, date_of_birth, expiry_date)
        self.id_number = id_number

class Drivers_License(AbstractPrimaryDocument):
    def __init__(self, first_name, last_name, nationality, gender,
                 date_of_birth, expiry_date):
        super(Drivers_License,self).__init__(first_name, last_name, nationality,
                                             gender, date_of_birth, expiry_date)

class Passport(AbstractPrimaryDocument):
    def __init__(self, first_name, last_name, nationality, gender,
                 date_of_birth, expiry_date):
        super(Passport,self).__init__(first_name, last_name, nationality,
                                      gender, date_of_birth, expiry_date)

from datetime import date, timedelta # for date math in EyeTest

class EyeTest(AbstractPrimaryDocument):
    def __init__(self, first_name, last_name, nationality, gender,
                 date_of_birth, expiry_date):
        # Eye Tests expire after 30 days
        if expiry_date is None:
            super(EyeTest,self).__init__(first_name, last_name, nationality,
                                         gender, date_of_birth,
                                         date.today() + timedelta(days=30))
        else:
            super(EyeTest,self).__init__(first_name, last_name, nationality,
                                         gender, date_of_birth, expiry_date)
        

class Drivers_License_Translation(object):
    def __init__(self,drivers_license):
        self.drivers_license = drivers_license

class Customer(object):
    def __init__(self, emirates_id, drivers_license, passport, eye_test,
                 drivers_license_translation):
        self.emirates_id = emirates_id
        self.drivers_license = drivers_license
        self.passport = passport
        self.eye_test = eye_test
        self.drivers_license_translation = drivers_license_translation

# For simplicity, this just has a single member representing the Customer
class UAE_Drivers_License(object):
    def __init__(self,driver):
        self.driver = driver
