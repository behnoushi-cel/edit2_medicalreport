from assignments.model.entity import *


class MedicalReport(Base):
    __tablename__ = "medical_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(DateTime)
    description = Column(String(30), nullable=False)

    patient_id = Column(Integer, ForeignKey("patient_tbl.id"))
    patient = relationship(Patient)

    doctor_id = Column(Integer, ForeignKey("doctor_tbl.id"))
    doctor = relationship(Doctor)

    def __init__(self, patient, doctor, date_time, description):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
        self.description = description

    # todo : getter / setter (validation)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 30:
            self._description = value
        else:
            raise ValueError("Description must be a string with 1 to 30 characters")
