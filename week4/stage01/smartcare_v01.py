# Task 1
# Create and run a simple Python file with basic input/output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = "Alice Smith"
practitioner1_name = "Dr. John Doe"
appointment1_time = "2024-07-20 10:00 AM"

print(
    f"Patient: {patient1_name} | "
    f"Practitioner: {practitioner1_name} | "
    f"Time: {appointment1_time}"
)

# Second Appointment
patient2_name = "Bob Johnson"
practitioner2_name = "Dr. Jane Roe"
appointment2_time = "2024-07-20 11:30 AM"

print(
    f"Patient: {patient2_name} | "
    f"Practitioner: {practitioner2_name} | "
    f"Time: {appointment2_time}"
)


# Task 1 Enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)


def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )


print("Welcome to SmartCare: The Clinical Appointment Booking System!")

book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2024-07-20 10:00 AM"
)

book_appointment(
    "Bob Johnson",
    "Dr. Jane Roe",
    "2024-07-20 11:30 AM"
)

display_appointments()


# Part F - Verify Behaviour

print("\n--- Test 1: Normal appointment ---")

book_appointment(
    "Sarah Smith",
    "Dr. John Doe",
    "2024-07-20 2:00 PM"
)

display_appointments()


print("\n--- Test 2: Blank patient name ---")

try:
    book_appointment(
        "",
        "Dr. John Doe",
        "2024-07-20 3:00 PM"
    )
except ValueError as error:
    print("Error caught:", error)


print("\n--- Test 3: Same practitioner and time ---")

book_appointment(
    "Tom Brown",
    "Dr. Jane Roe",
    "2024-07-20 11:30 AM"
)

display_appointments()


print("\n--- Test 4: Strange input ---")

try:
    book_appointment(
        None,
        "Dr. John Doe",
        None
    )
except ValueError as error:
    print("Error caught:", error)

