from .typeValidator import *
import validator.typeValidator as typeValidator
import services.HumanResourcesService as HumanResourcesService

def createEmployee(Hos,rol):
    fullname=input("ingrese nombre completo del " + rol + ":")
    textValidator(fullname,"nombre de " + rol+ ":")
    id=numberValidator(input("ingrese la cedula de " + rol + ":"), "cedula de " + rol +":")
    email=input("ingrese correo electronico del " + rol + ":")
    textValidator(fullname,"correo electronico de " + rol + ":")
    phonenumber=input("ingrese numero de telefono del " + rol + ":")
    textValidator(fullname,"numero telefono de " + rol + ":")
    birthdate=input("ingrese Fecha de nacimiento del " + rol + ":")
    textValidator(fullname,"fecha de nacimiento de " + rol + ":")
    address=input("ingrese direccion del " + rol + ":")
    textValidator(fullname,"direccion de " + rol + ":")
    rol="opcion invalida"
    while rol == "opcion invalida":
        print("Selecciona el rol del empleado:")
        rol=input("1.adminRH\n2.PersonalAdmin\n3.doctor\n4.Enfermera\n")
        rol=typeValidator.assignrole(rol)
    username=input("ingrese usuario del " + rol + ":")
    textValidator(username,"usuario de " + rol + ":")
    password=input("ingrese contraseña del " + rol + ":")
    textValidator(password,"contraseña de " + rol + ":")
    HumanResourcesService.createEmployee(Hos,id,fullname,email,phonenumber,birthdate,address,rol,username,password)
    
   