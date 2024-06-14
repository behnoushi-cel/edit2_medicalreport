import re
from datetime import datetime,date


class Validator:
    @classmethod
    def name_validator(cls, name, family):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def patient_validator(cls, name, family):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", name):
            return Patient
        else:
            raise ValueError(message)

