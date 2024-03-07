from model import models
from services import loginService
from validator import userTypeValidator

Hospital=models.Hospital()
adminRH=models.employee(1,"juan sebastian cardona bran","juancar@gmail.com","3116697008","17/09/2000","Cr69B#37-05","adminRH","juansebz","123")
Hospital.employees.append(adminRH)
MainMenu="1.Iniciar sesion\n0. Salir\n"

def CreateUser(Hos):
    try:
        userTypeValidator.createUser(Hos,"usuario")
    except Exception as error:
        print(str(error))

def MenuAdminRH(Hos,user):
    while True:
        option=input("1. Crear nuevo usuario\n 2.eliminar usuario\n 3. gestionar permisos de usuario\n 4. Actualizacion de datos personales\n  5.Listar todos los usuarios\n 6.Cerrar sesion\n")
        if option=="1":
            CreateUser(Hos)
        if option=="6":
            print("Cerrando sesion")
            return
          
def MenuDoctor(Hos,user):
    option=input("1. ver historial clinico\n 2.Crear nuevo registro médico\n 3.Actualizar registro médico existente\n 4. Prescribir tratamiento\n 5. Ordenar pruebas médicas\n 6. Cerrar sesión")

def MenupersonAdmin(Hos,user):
    option=input("1.Registrar paciente\n 2. Programar cita para paciente \n 3.Registrar informacion de facturacion \n 4. Ver historial y registros de un paciente \n 5. Listar todos los pacientes \n 6.Cerrar sesion")

def MenuNurse(Hos,user):
    option=input("1. Registrar datos vitales de un paciente\n 2. Registrar medicamentos administrados\n 3. Registrar procedimientos realizados\n 4. Registrar pruebas médicas\n 5. Ver observaciones y detalles de la atención del paciente\n 6. Cerrar sesión")

def LoginRouter(Hos,user):
    print(user.rol)
    if user.rol=="adminRH":
       MenuAdminRH(Hos,user)
    elif user.rol=="doc":
        MenuDoctor(Hos,user)
    elif user.rol=="PersonAdmin":
        MenupersonAdmin(Hos,user)
    elif user.rol=="nurse":
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
       user=loginService.userSearch(Hospital,username)
    
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
    