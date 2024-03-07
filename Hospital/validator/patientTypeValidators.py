from .typeValidator import *
import services.HospitalService as HospitalService
def createPatient(Hospital):
    id=len(Hospital.Patient)
    name=input("ingrese nombre del paciente " + str(id))
    textValidator(name,"nombre de paciente" + str(id))
    companionId=numberValidator(input("ingrese la cedula del acompañante" + name), "cedula del acompañante " + name)
    age=numberValidator(input("ingrese la edad de " + name), "edad de " + name)
    gender=input("ingrese la genero del paciente " + name)
    textValidator(gender,"genero" + name)
    weigth=numberValidator(input("ingrese el peso de " + name), "edad de " + name)
    features=input("ingrese enfermedades" + name)
    textValidator(features,"las enfermedades " + name)
    HospitalService.createPatient(Hospital,id,name,companionId,age,gender,weigth,features)

   