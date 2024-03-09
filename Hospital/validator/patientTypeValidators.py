from .typeValidator import *
import services.PersonalAdminService as PersonalAdminService

def createPatient(Hos,rol):
    fullname=input("ingrese nombre del " + rol + ":")
    textValidator(fullname,"nombre de " + rol + ":")
    id=numberValidator(input("ingrese la cedula de " + rol + ":"), "cedula de " + rol + ":")
    gender=input("ingrese genero del " + rol + ":")
    textValidator(fullname,"genero de " + rol + ":")
    email=input("ingrese correo electronico del " + rol + ":")
    textValidator(fullname,"correo electronico de " + rol + ":")
    phonenumber=input("ingrese numero de telefono del " + rol + ":")
    textValidator(fullname,"numero telefono de " + rol + ":")
    birthdate=input("ingrese Fecha de nacimiento del " + rol + ":")
    textValidator(fullname,"fecha de nacimiento de " + rol + ":")
    address=input("ingrese direccion del " + rol + ":")
    textValidator(fullname,"direccion de " + rol + ":")
    Contactname=input("ingrese nombre del acompañante " + ":")
    textValidator(fullname,"nombre del acompañante " + rol + ":")
    patientrelationship=input("ingrese relacion del acompañante " + ":")
    textValidator(fullname,"relacion del acompañante " + rol + ":")
    insuranceCompany=input("ingrese compañia de seguros del" + rol + ":")
    textValidator(fullname,"compañia de seguros " + rol + ":")
    policynumber=input("ingrese numero de poliza del " + rol + ":")
    textValidator(fullname,"numero poliza de " + rol + ":")
    statePolicy=input("ingrese el estado de poliza del" + rol + ":")
    textValidator(fullname,"estado de poliza " + rol + ":")
    policyValidity=input("ingrese vigencia de poliza del" + rol + ":")
    textValidator(fullname,"vigencia de poliza del" + rol + ":")
    PersonalAdminService.CreatePatient(Hos,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity)

   