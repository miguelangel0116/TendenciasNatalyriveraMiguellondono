from model import models
from services import loginService
from validator import userTypeValidator
from validator import patientTypeValidators
from validator import DoctorValidator
from services.PersonalAdminService import getPatientById
from validator import NurseValidator




Hospital=models.Hospital()
adminRH=models.Employee(1036765433,"juan sebastian cardona bran","juancar@gmail.com","3116697008","17/09/2000","Cr69B#37-05","adminRH","juansebz","123")
PersonalAdmin=models.Employee(1035278877,"Nataly rivera agudelo","Nata@gmail.com","3246936436","19/03/2005","Cr68B#34-07","PersonalAdmin","nata","340")
Doctor=models.Employee(1027255500,"Alejandro zarate cano","Alejozarate@gmail.com","3125854741","20/04/2000","Cr64B#35c-02","doctor","alejo","234")
Nurse=models.Employee(1025225566,"Paulina tobon","pau@gmail.com","3225679848","19/05/2000","Cr69B#34-06","Nurse","nurse","222")
patient = models.Patient(1,"Karla Monsalve", "Femenino", "karlamonsalve@gmail.com", "3213456", "12/03/2004", "Cl 31#69-32", "Lorenzo Aguirre", "Tío" , "seguros xlf", "11212", "activa", "12/09/2013")
Hospital.employees.append(adminRH)
Hospital.employees.append(PersonalAdmin)
Hospital.employees.append(Doctor)
Hospital.employees.append(Nurse)
Hospital.patients.append(patient)

Hospital.clinicalHistory["1"] ={}
Hospital.visitsHistory["1"] ={}

MainMenu="1.Iniciar sesion\n0. Salir\n"

#------ METODOS -------#

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

def createMedicalHistory(Hospital,patientId,user):
    try:
        doctorId = user.id
        DoctorValidator.createMedicalHistoryQuery(Hospital,patientId,doctorId)
        print("Historia clinica creada")
    except Exception as error:
        print(str(error))


def searchPatient(hospital, user):
    try:
        patient_id = input("Ingrese el ID del paciente a buscar: ")
        patient = getPatientById(hospital, int(patient_id))
        if patient:
            printPatientData(patient)
        else:
            print("No se encontró un paciente con ese ID.")
    except ValueError as error:
        print(str(error))

def printPatientData(patient):
    print(f"Nombre: {patient.fullname}")
    print(f"Género: {patient.gender}")
    print(f"Correo electronico: {patient.email}")
    print(f"Numero de telefono: {patient.phonenumber}")
    print(f"Fecha de nacimiento: {patient.birthdate}")
    print(f"Direccion: {patient.address}")
    print(f"Nombre contacto de emergencia: {patient.Contactname}")
    print(f"Relacion: {patient.patientrelationship}")
    print(f"Compañia de seguros: {patient.insuranceCompany}")
    print(f"Numero de poliza: {patient.policynumber}")
    print(f"Estado de poliza: {patient.statePolicy}")
    print(f"Fecha de vigencia de la poliza: {patient.policyValidity}")



def getHistoryClinicPatient(hospital, patientId):
    try:
        DoctorValidator.getHistoryClinicQuery(hospital, patientId)
    except Exception as error:
        print(str(error))

def createHistoryVisits(Hospital,id):
    try:
        NurseValidator.createHistoryVisitsQuery(Hospital,id)
        print("se creo la visita correctamente")
    except Exception as error:
        print(str(error))

def getHistoryVisitsPatient(Hospital,id):
    try:
        NurseValidator.getHistoryVisitsQuery(Hospital,id)
    except Exception as error:
        print(str(error))


#----- MENUS -------#

def MenuAdminRH(Hos,user):
    while True:
        option=input("1. Crear empleado\n 2.eliminar empleado\n 3. Actualizacion datos del empleado\n  4.Listar todos los usuarios de empleados\n 5.Cerrar sesion\n")
        if option=="1":
            CreateUser(Hos)

        if option=="2":
            DeleteEmployee(Hos)
        
        if option =="3":
            username_to_update = input("Ingrese el username del empleado que desea actualizar: ")
            user_to_update = loginService.SearchEmployee(Hos, username_to_update)
            if user_to_update:
                userTypeValidator.updateEmployee(Hos, user_to_update)
        if option=="4":
             userTypeValidator.listAllEmployees(Hos)
           
        if option=="5":
            print("Cerrando sesion...")
            return
          
def MenupersonalAdmin(Hos,user):
    while True:
        option=input("1.Crear paciente\n 2. Actualizar paciente \n 3.programar cita para paciente \n 4. Listar todos los pacientes\n 5. Generar factura\n 6.Cerrar sesion")
        if option=="1":
            CreatePatient(Hos) 
        if option=="2":
            id_to_update = input("Ingrese la cédula del paciente que desea actualizar: ")
            try:
                patientTypeValidators.updatePatient(Hos, id_to_update)
            except Exception as error:
                print(str(error))
        if option=="3":
            patientTypeValidators.scheduleAppointment(Hos)
        if option=="4":
            patientTypeValidators.listAllPatients(Hos)
        if option=="5":
            pass
        if option=="6":
           print("Cerrando sesion...")
           return

def MenuDoctor(Hos,user):
    while True:
        option=input("1. ver datos del paciente\n 2.Crear registro medico\n 3.Mostrar la historia clinica de un paciente\n 4. Cerrar sesion\n")
        if option=="1":
         searchPatient(Hospital, user)
        if option=="2":
          patientId = int(input("Ingrese la cedula (ID) del paciente: "))
          createMedicalHistory(Hospital,patientId,user) 
        if option=="3":
          patientId = int(input("Ingrese la cedula (ID) del paciente: "))
          getHistoryClinicPatient(Hospital,patientId)
        if option=="4":
            print("Cerrar sesion...")
            return

def MenuNurse(Hos,user):
    option = input("1.Agregar historia de visitas\n2.Mostrar registro de visitas\n3.Ver datos del paciente\n4.Cerrar sesión\n")
    if option == "1":
       id = int(input("Ingrese la cedula (ID) del paciente: "))
       createHistoryVisits(Hospital,id)  
    if option=="2":
        id = int(input("Ingrese la cedula (ID) del paciente: "))
        getHistoryVisitsPatient(Hospital,id)
    if option=="3":
        searchPatient(Hospital, user)
    if option=="4":
        print("Cerrando sesion...")
        return
            
            
#------ ROUTER DE MENUS -------#
        
def LoginRouter(Hos,user):
    print("---Bienvenid@---")
    print(user.rol)
    if user.rol=="adminRH":
       MenuAdminRH(Hos,user)
    elif user.rol=="doctor":
        MenuDoctor(Hos,user)
    elif user.rol=="PersonalAdmin":
        MenupersonalAdmin(Hos,user)
    elif user.rol=="Nurse":
        MenuNurse(Hos,user)
    else:
        print("El usuario no tiene un rol valido")
    

while True:
    option = input(MainMenu)
    print("Ha elegido la opción:", option)
    if option == "1":
        print("Ingrese su usuario:")
        username = input()
        password = input("Ingrese su contraseña:\n")
        user = loginService.SearchEmployee(Hospital, username)
        if user == None:
            print("Usuario no encontrado")
            continue
        if user.password != password:
            print("Error en usuario o contraseña")
            continue
        LoginRouter(Hospital, user)
    if option == "0":

        print("¡Hasta pronto!")
        break