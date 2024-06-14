from assignments.model.entity import *


class Patient(Base):
    __tablename__ = "patient_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    national_id = Column(String(10), nullable=False, unique=True)
    phone = Column(String(15), nullable=False)
    birth_date = Column(Date, nullable=False)

    # todo : national_id, phone, birth_date



    medical_report = relationship("MedicalReport", back_populates="patient")

    def __init__(self, name, family):
        self.person_id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone = phone
        self.birth_date = birth_date

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





    # todo : getter / setter (validation)

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

    # Getter and Setter for birth_date
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        # Add any date validation if necessary
        self._birth_date = value