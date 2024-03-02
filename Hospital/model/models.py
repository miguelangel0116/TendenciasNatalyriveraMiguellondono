import datetime

class Person():
    def __init__(self,id,name,userName,password,age,rol):
        self.id=id
        self.name=name
        self.userName=userName
        self.password=password
        self.age=age
        self.rol=rol


class patient():
    def __init__(self,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber):
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
        


class HumanResources():
    def __init__(self,id,fullname,email,phonenumber,birthdate,address,role,username,password):
        self.id=id
        self.fullname=fullname
        self.email=email
        self.phonenumber=phonenumber
        self.birthdate=birthdate
        self.address=address
        self.role=role
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
        self.persons=[]
        self.patients=[]
        self.orders=[]
        self.invoices=[]
        self.clinicalHistory={}
        

