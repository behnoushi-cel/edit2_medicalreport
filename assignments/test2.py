
pip install mysql-connector-python
from datetime import datetime


class Doctor:
    def __init__(self, doctor_id, name, family, skills):
        self.doctor_id = doctor_id
        self.name = name
        self.family = family
        self.skills = skills


class Patient:
    def __init__(self, patient_id, name, family, disease):
        self.patient_id = patient_id
        self.name = name
        self.family = family
        self.disease = disease


class MedicalReport:
    def __init__(self, doctor, patient):
        self.doctor = doctor
        self.patient = patient
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_report(self):
        print(f"Medical Report - Date and Time: {self.date_time}\n")
        print(f"Doctor ID: {self.doctor.doctor_id}")
        print(f"Doctor Name: {self.doctor.name} {self.doctor.family}")
        print(f"Doctor Skills: {', '.join(self.doctor.skills)}\n")
        print(f"Patient ID: {self.patient.patient_id}")
        print(f"Patient Name: {self.patient.name} {self.patient.family}")
        print(f"Patient Disease: {self.patient.disease}")


# Example usage
doctor = Doctor(doctor_id=1, name="John", family="Doe", skills=["Cardiology", "Internal Medicine"])
patient = Patient(patient_id=101, name="Jane", family="Smith", disease="Hypertension")

report = MedicalReport(doctor, patient)
report.display_report()
