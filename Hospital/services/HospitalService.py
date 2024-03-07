from .HumanResourcesService import validateId
import model.models as models
import datetime
def createPatient(Hospital,id,name,companionId,age,gender,weigth,features):
    companion= validateId(Hospital,companionId)
    if companion== None:
        raise Exception("no existe un acompañante con esa cedula")
    Patient=models.patient(id,name,companionId,age,gender,weigth,features)
    Hospital.patient.append(Patient)
    Hospital.clinicalHistory[str(id)]={}
    print("Paciente creado")

def createMedicalQuery(veterinary,consultationReason,symptomatology,diagnosis,procedure,procedureDetail,medicine,medicineDose,petId,user):
    if str(petId) not in veterinary.clinicalHistory:
        raise Exception("no existe la mascota")
    newClinicalHistory={}
    newClinicalHistory["consultationReason"]=consultationReason
    newClinicalHistory["symptomatology"]=symptomatology
    newClinicalHistory["diagnosis"]=diagnosis
    date=datetime.date.today()
    if procedure!="N/A":
        newClinicalHistory["procedure"]=procedure
        newClinicalHistory["procedureDetail"]=procedureDetail
    if medicine != "N/A":
        owner=findPet(veterinary,petId)
        order=models.Order(len(veterinary.orders),owner.id,petId,user.id,medicine,date)
        veterinary.orders.append(order)
        newClinicalHistory["medicine"]=medicine
        newClinicalHistory["medicineDose"]=medicineDose
        newClinicalHistory["orderId"]=order.id
    print(date)
    print("nueva historia clinica")
    print(newClinicalHistory)
    veterinary.clinicalHistory[str(petId)][date]=newClinicalHistory
    print("historia clinica")
    print(veterinary.clinicalHistory[str(petId)])
    print("historia clinica veterinatia")
    print(veterinary.clinicalHistory)
   


def findPet(veterinary, petId):
    for pet in veterinary.pets:
        if pet.id==petId:
            return pet
    return None
    