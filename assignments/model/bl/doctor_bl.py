from assignments.controller.exceptions.exceptions import doctorNotFoundError
from assignments.model.da.da import DataAccess
from assignments.model.entity.doctor import Doctor

# Initialize DataAccess with Doctor class
doctor_da = DataAccess(Doctor)

class ClassDoctorBl:

    @staticmethod
    def save(doctor):
        return doctor_da.save(doctor)

    @staticmethod
    def edit(doctor):
        if doctor_da.find_by_id(doctor.id):
            return doctor_da.edit(doctor)
        else:
            raise doctorNotFoundError()

    @staticmethod
    def remove(id):
        doctor = doctor_da.find_by_id(id)
        if doctor:
            return doctor_da.remove(doctor)
        else:
            raise doctorNotFoundError()

    @staticmethod
    def find_all():
        doctor_list = doctor_da.find_all()
        if doctor_list:
            return doctor_list
        else:
            raise doctorNotFoundError()

    @staticmethod
    def find_by_id(id):
        doctor = doctor_da.find_by_id(id)
        if doctor:
            return doctor
        else:
            raise doctorNotFoundError()

    @staticmethod
    def find_by_family(family):
        doctor_list = doctor_da.find_by(Doctor.family == family)
        if doctor_list:
            return doctor_list
        else:
            raise doctorNotFoundError()
