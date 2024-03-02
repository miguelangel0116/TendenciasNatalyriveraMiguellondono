from model import models
from services import loginService
#
Hospital=models.Hospital()
adminRH=models.Person(1,"juanse","juansebz","123","23","adminRH")

Hospital.persons.append(adminRH)
Menu="1.Iniciar sesion\n0. Salir\n"

def MenuAdminRH(Hos,user):
    option=input("1. Crear nuevo usuario\n 2.eliminar usuario\n 3. gestionar permisos de usuario\n 4. Actualizacion de datos personales\n  5.Listar todos los usuarios\n 6.Cerrar sesion")
    
def MenuDoctor(Hos,user):
    option=input("1. ver historial clinico\n 2.Crear nuevo registro médico\n 3.Actualizar registro médico existente\n 4. Prescribir tratamiento\n 5. Ordenar pruebas médicas\n 6. Cerrar sesión")


def MenuSeller(Hos,user):
    pass
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
    elif user.rol=="seller":
        MenuSeller(Hos,user)
    elif user.rol=="PersonAdmin":
        MenupersonAdmin(Hos,user)
    elif user.rol=="nurse":
        MenuNurse(Hos,user)
    else:
        print("El usuario no tiene un rol valido")
    
while True:
    option=input(Menu)
    print("Has elegido la opcion",option)
    if option=="1":
       print("Ingrese su usuario:")
       userName=input()
       password=input("Ingrese su contraseña:\n")
       user=loginService.userSearch(Hospital,userName)
    
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
    