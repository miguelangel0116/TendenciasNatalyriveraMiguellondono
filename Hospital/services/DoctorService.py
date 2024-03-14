from .HumanResourcesService import validateId
import model.models as models
import datetime

def createMedicalQuery(Hospital, patientId, idDoctor, consultationReason, symptoms, diagnosis, diagnosisAid, medications, procedures):
    patient = validateId(Hospital, str(patientId))
    if patient is None:
        raise Exception("El paciente no existe")
    date = datetime.date.today()
    newClinicalHistory = {}
    newClinicalHistory["date"] = date
    newClinicalHistory["idDoctor"] = idDoctor
    newClinicalHistory["consultationReason"] = consultationReason
    newClinicalHistory["symptoms"] = symptoms
    newClinicalHistory["diagnosis"] = diagnosis
    if diagnosisAid != "N/A":
        order = models.Order(len(Hospital.orders), patient.id, date, "N/A", "N/A", diagnosisAid)
        Hospital.orders.append(order)
    if diagnosisAid == "N/A":
        newClinicalHistory["medications"] = medications
        newClinicalHistory["procedures"] = procedures
        order = models.Order(len(Hospital.orders), patient.id, date, medications, procedures, "N/A")
        Hospital.orders.append(order)
    if str(patient.id) not in Hospital.clinicalHistory:
        Hospital.clinicalHistory[str(patient.id)] = {}
    if date not in Hospital.clinicalHistory[str(patient.id)]:
        Hospital.clinicalHistory[str(patient.id)][date] = []
    Hospital.clinicalHistory[str(patient.id)][date].append(newClinicalHistory)
    print("Historia clinica agregada con exito")
    print(Hospital.clinicalHistory)