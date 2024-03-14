import model.models as models
def validateId(Hos,id):
    for employee in Hos.employees:
        if employee.id==id:
            return employee
    return None
def validateUserName(Hos,username):
    for employee in Hos.employees:
        if employee.username==username:
            return employee
    return None

def createEmployee(Hos, id, fullname, email, phonenumber, birthdate, address, rol, username, password):
    user = validateId(Hos, id)
    if user:
        raise Exception("Ya existe un usuario con esa cédula registrada")
    user = validateUserName(Hos, username)
    if user:
        raise Exception("Ya existe un usuario con ese username registrado")

    user = models.employee(id, fullname, email, phonenumber, birthdate, address, rol, username, password)
    Hos.employees.append(user)
    print("Empleado: {} creado con éxito".format(user.fullname))

def deleteUser(Hos, id):
    user = validateId(Hos, id)
    if user:
        Hos.employees.remove(user)
        print(f"Empleado con cédula {id} eliminado con éxito")
    else:
        raise Exception("No existe un usuario con esa cédula")
    
def validateId(Hos, id):
    for employee in Hos.employees:
        if employee.id == id:
            return employee
    return None
 
def updateEmployee(Hos, user):
    # Implementa la lógica de actualización aquí
    # Puedes pedir al usuario que ingrese los nuevos datos o proporcionar un formulario, etc.
    new_fullname = input(f"Ingrese el nuevo nombre completo para {user.username}: ")
    new_email = input(f"Ingrese el nuevo correo electrónico para {user.username}: ")
    new_phonenumber = input(f"Ingrese el nuevo número de teléfono para {user.username}: ")

    # Actualiza los datos del usuario
    user.fullname = new_fullname
    user.email = new_email
    user.phonenumber = new_phonenumber

    print(f"Datos de {user.username} actualizados con éxito.")
