import datetime

class Patient():
    def __init__(self,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity):
        self.id=id
        self.fullname=fullname
        self.gender=gender
        self.email=email
        self.phonenumber=phonenumber
        self.birthdate=birthdate
        self.address=address
        self.Contactname=Contactname
        self.patientrelationship=patientrelationship
        self.insuranceCompany=insuranceCompany
        self.policynumber=policynumber
        self.statePolicy=statePolicy
        self.policyValidity=policyValidity


class employee():
    def __init__(self,id,fullname,email,phonenumber,birthdate,address,rol,username,password):
        self.id=id
        self.fullname=fullname
        self.email=email
        self.phonenumber=phonenumber
        self.birthdate=birthdate
        self.address=address
        self.rol=rol
        self.username=username
        self.password=password


class Order():
    def __init__(self,id,patientId,doctorId,medicine,dose):
        self.id=id
        self.patientId=patientId
        self.doctorId=doctorId
        self.medicine=medicine
        self.dose=dose
        self.date=datetime.datetime.now


class Invoice():
    def __init__(self,id,patientId,patientname,patientage,doctorname,insuranceCompany,daysvalidity,policyEndDate):
        self.id=id
        self.patientId=patientId
        self.patientage=patientage
        self.patientname=patientname
        self.doctorname=doctorname
        self.insuranceCompany=insuranceCompany
        self.daysvalidity=daysvalidity
        self.policyEndDate=policyEndDate
        

class Hospital():
    def __init__(self):
        self.employees=[]
        self.patients=[]
        self.orders=[]
        self.invoices=[]
        self.clinicalHistory={}
        

