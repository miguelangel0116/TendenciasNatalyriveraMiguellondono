from model import models
from services import loginService
from validator import userTypeValidator
from validator import patientTypeValidators


Hospital=models.Hospital()
adminRH=models.employee(1,"juan sebastian cardona bran","juancar@gmail.com","3116697008","17/09/2000","Cr69B#37-05","adminRH","juansebz","123")
PersonalAdmin=models.employee(2,"Nataly rivera agudelo","Nata@gmail.com","3246936436","19/03/2005","Cr68B#34-07","PersonalAdmin","nata","340")
Doctor=models.employee(3,"Alejandro zarate cano","Alejozarate@gmail.com","3125854741","20/04/2000","Cr64B#35c-02","doctor","alejo","234")
Hospital.employees.append(adminRH)
Hospital.employees.append(PersonalAdmin)
Hospital.employees.append(Doctor)
MainMenu="1.Iniciar sesion\n0. Salir\n"


def CreateUser(Hos):
    try:
        userTypeValidator.createEmployee(Hos,"empleado")
    except Exception as error:
        print(str(error))

def CreatePatient(Hos):
    try:
        patientTypeValidators.createPatient(Hos,"paciente")
    except Exception as error:
        print(str(error))

def DeleteEmployee(Hos):
    try:
        userTypeValidator.deleteUser(Hos, user)
    except Exception as error:
        print(str(error))

def MenuAdminRH(Hos,user):
    while True:
        option=input("1. Crear empleado\n 2.eliminar empleado\n 3. Actualizacion datos del paciente\n  4.Listar todos los usuarios empleados\n 5.Cerrar sesion\n")
        if option=="1":
            CreateUser(Hos)

        if option=="2":
            DeleteEmployee(Hos)
        
        if option =="3":
            username_to_update = input("Ingrese el username del empleado que desea actualizar: ")
            user_to_update = loginService.SearchEmployee(Hos, username_to_update)
            if user_to_update:
                userTypeValidator.updateEmployee(Hos, user_to_update)
            
        if option=="5":
            print("Cerrando sesion")
            return
          
def MenuDoctor(Hos,user):
    option=input("1. ver datos del paciente\n 2.Generar historia clinica\n 3.Cerrar sesion\n")

def MenupersonAdmin(Hos,user):
    while True:
        option=input("1.Crear paciente\n 2. Actualizar paciente \n 3.programar cita para paciente \n 4. Listar todos los pacientes\n 5. Cerrar sesion\n ")
        if option=="1":
            CreatePatient(Hos) 
        if option=="5":
           print("Cerrando sesion")
           return

def MenuNurse(Hos,user):
    option=input("1. Registrar datos vitales del paciente\n 2. Generar registro de visita\n 3. Cerrar sesión")

def LoginRouter(Hos,user):
    print(user.rol)
    if user.rol=="adminRH":
       MenuAdminRH(Hos,user)
    elif user.rol=="doctor":
        MenuDoctor(Hos,user)
    elif user.rol=="PersonalAdmin":
        MenupersonAdmin(Hos,user)
    elif user.rol=="Enfermera":
        MenuNurse(Hos,user)
    else:
        print("El usuario no tiene un rol valido")
    


while True:
    option=input(MainMenu)
    print("Has elegido la opcion",option)
    if option=="1":
       print("Ingrese su usuario:")
       username=input()
       password=input("Ingrese su contraseña:\n")
       user=loginService.SearchEmployee(Hospital,username)
    if user==None:
        print("El usuario no se encontro")
        continue
    if user.password!=password:
       print("usuario o contraseña incorrecto")
       continue
    LoginRouter(Hospital,user)
    
    if option=="0":
        print("Hasta pronto")
        break
    