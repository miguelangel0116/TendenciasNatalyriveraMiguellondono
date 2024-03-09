def textValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor valido")

def numberValidator(string,element):
    textValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")
    

def assignrole(role):
    roleSelection = {
    "1": "adminRH",
    "2": "PersonaAdmin",
    "3": "doctor",
    "4": "Enfermera",
    }
    return roleSelection.get(role, "Opción inválida")
