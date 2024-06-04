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
    def get_description(self):
        return self.description

    def set_description(self, description):
        if isinstance(description, str) and description.lower() in ("income", "outcome"):
            self.medica_report = description.lower()
        elif isinstance(description, int) and description in (1, -1):
            self.description = "income" if description == 1 else "outcome"
        else:
            raise ValueError("invalid:transaction_type")