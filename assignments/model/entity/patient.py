
from sqlalchemy import Column, Integer, String, Boolean

from model.entity.base import Base
from assignments.model.entity import *


class Patient(Base):
    __tablename__ = "patient_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    medicalreport = relationship(medicalreport, backref="patient")
    # todo : national_id, phone, birth_date

    medical_report = relationship("MedicalReport", back_populates="patient")

    def __init__(self, name, family):
        self.person_id = None
        self.name = name
        self.family = family


    # todo : getter / setter (validation)