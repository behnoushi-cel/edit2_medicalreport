
class PatientNotFoundError(Exception):
    def __init__(self):
        super().__init__("Patient not found")

class PatientController:
    @staticmethod
    def find_all():
        # Replace with actual logic to retrieve all patients
        return []

    @staticmethod
    def save(name, family):
        # Replace with actual logic to save a patient
        return True, "Patient saved successfully"

    @staticmethod
    def edit(id, name, family):
        # Replace with actual logic to edit a patient
        patient = PatientController.find_by_id(id)
        if not patient:
            raise PatientNotFoundError()
        patient.name = name
        patient.family = family
        # Save the updated patient
        return True, "Patient updated successfully"

    @staticmethod
    def remove(id):
        # Replace with actual logic to remove a patient
        patient = PatientController.find_by_id(id)
        if not patient:
            raise PatientNotFoundError()
        # Logic to remove patient
        return True, "Patient removed successfully"

    @staticmethod
    def find_by_id(id):
        # Replace with actual logic to find a patient by ID
        return None)