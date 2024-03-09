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

    
 

