from enum import Enum

from patient import Patient
from practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class Appointment:
    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        appointment_time: str
    ):
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")

        self._status = AppointmentStatus.CANCELLED