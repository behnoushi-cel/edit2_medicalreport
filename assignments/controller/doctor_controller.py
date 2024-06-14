from assignments.model import Doctor
from assignments.business_logic import DoctorBl

class DoctorNotFoundError(Exception):
    def __init__(self):
        super().__init__("Doctor not found")

class DoctorController:
    @staticmethod
    @exception_handling
    def save(name, family, skill):
        doctor = Doctor(name, family, skill)
        DoctorBl.save(doctor)

    @staticmethod
    @exception_handling
    def edit(id, name, family, skill):
        doctor = DoctorBl.find_by_id(id)
        if doctor is None:
            raise DoctorNotFoundError()
        doctor.name = name
        doctor.family = family
        doctor.skill = skill
        DoctorBl.save(doctor)

    @staticmethod
    @exception_handling
    def remove(id):
        doctor = DoctorBl.find_by_id(id)
        if doctor is None:
            raise DoctorNotFoundError()
        DoctorBl.delete(doctor)

