# todo : complete file

class MedicalReportBl:
    @classmethod
    def save(cls, session, medical_report):
        """
        Save a new medical report to the database.
        """
        session.add(medical_report)
        session.commit()

    @classmethod
    def update(cls, session, medical_report_id, **kwargs):
        """
        Update an existing medical report.
        """
        medical_report = session.query(MedicalReport).filter_by(id=medical_report_id).first()
        if not medical_report:
            raise ValueError("Medical report not found")

        for key, value in kwargs.items():
            if hasattr(medical_report, key):
                setattr(medical_report, key, value)

        session.commit()

    @classmethod
    def delete(cls, session, medical_report_id):
        """
        lDelete a medical report from the database.
        """
        medical_report = session.query(MedicalReport).filter_by(id=medical_report_id).first()
        if not medical_report:
            raise ValueError("Medical report not found")

        session.delete(medical_report)
        session.commit()

    @classmethod
    def get_by_id(cls, session, medical_report_id):
        """
        Retrieve a medical report by its ID.
        """
        return session.query(MedicalReport).filter_by(id=medical_report_id).first()

    @classmethod
    def get_all(cls, session):
        """
        Retrieve all medical reports.
        """
        return session.query(MedicalReport).all()
