from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus


# Test 1 - Create valid objects

patient = Patient("John Smith")

practitioner = Practitioner(
    "P001",
    "Dr Sarah Jones",
    "General Practice"
)

appointment = Appointment(
    patient,
    practitioner,
    "10:00 AM"
)

print("Test 1 - Valid objects")
print("Patient:", patient.name)
print("Practitioner:", practitioner.name)
print("Appointment status:", appointment.status)


# Test 2 - Invalid patient name

print("\nTest 2 - Invalid patient name")

try:
    invalid_patient = Patient("")
except ValueError as error:
    print("Error caught:", error)


# Test 3 - Cancel scheduled appointment

print("\nTest 3 - Cancel appointment")

appointment.cancel()

print("Appointment status:", appointment.status)


# Test 4 - Attempt repeated cancellation

print("\nTest 4 - Repeated cancellation")

try:
    appointment.cancel()
except ValueError as error:
    print("Error caught:", error)