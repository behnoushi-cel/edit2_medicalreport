class PatientNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "patient not found")

class DoctorNotFoundError(Exception):
     def __init__(self):
         Exception.__init__(self, "doctor not found")

class Medical_reportNotFoundError(Exception):
    def __init__(self):
         Exception.__init__(self, "Medicalreport not found")


class ComponentNotFoundError(Exception):
    def __init__(self):
         Exception.__init__(self, "Component not found")
