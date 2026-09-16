class Appointment:
    def __init__(self, patient, practitioner, appointment_time, status):
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self.status = status

    def cancel(self):
        pass
