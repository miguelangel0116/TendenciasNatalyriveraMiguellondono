import model.models as models

def validateId(Hospital,id):
    for patient in Hospital.patients:
        if patient.id==id:
            return patient
    return None

def CreatePatient(Hospital,id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity):
     patient = validateId(Hospital, id)
     if patient:
      raise Exception ("Ya existe un paciente con esa cedula registrada")
     patient = models.Patient(id,fullname,gender,email,phonenumber,birthdate,address,Contactname,patientrelationship,insuranceCompany,policynumber,statePolicy,policyValidity)
     
     Hospital.clinicalHistory[str(id)]={}
     Hospital.patients.append(patient)
     print("Paciente: {} creado con éxito".format(patient.fullname))




