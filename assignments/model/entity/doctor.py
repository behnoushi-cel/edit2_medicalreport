from assignments.model.entity import *

from sqlalchemy import Column, Integer, String, Boolean

from model.entity.base import Base


class Doctor(Base):
    __tablename__ = "doctor_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    medicalreport = relationship(medicalreport, backref="doctor")
    skill = Column(String(50), nullable=False)
    # todo : national_id, phone, birth_date
    national_id = Column(String(10), nullable=False, unique=True)
    phone = Column(String(15), nullable=False)
    birth_date = Column(Date, nullable=False)

    medical_report = relationship("MedicalReport", back_populates="doctor")

    def __init__(self, name, family, skill):
        self.person_id = None
        self.name = name
        self.family = family
        self.skill = skill
        self.national_id = national_id
        self.phone = phone
        self.birth_date = birth_date

    # todo : getter / setter (validation)

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("National ID must be a 10-digit number")
        self._national_id = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise ValueError("Phone number must be at least 10 digits")
        self._phone = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        # Add any date validation if necessary
        self._birth_date = value