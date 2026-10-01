# Stage 1 Lab
## Human vs AI: Building Your First SmartCare Prototype

### Part A - Understand the Problem: AI OFF

#### What data must be stored?

- Patient name
- Practitioner name
- Appointment time

#### What functions might be useful?

- Add a new appointment
- Display existing appointments
- Cancel an appointment

#### What could go wrong?

- Patient name could be left empty.
- Practitioner name could be missing.
- Appointment time could be entered incorrectly.
- Patients or practitioners could be double booked.

#### What requirements are unclear?

- What format should be used for appointment times?
- Can appointments be edited or cancelled?
- How many appointments should be stored?

#### Limitations of the Prototype

1. The program only checks whether the patient name is empty.

2. It does not check whether the practitioner name is empty.

3. It does not check whether the appointment time is missing or entered
   incorrectly.

4. It does not prevent two appointments from being booked with the same
   practitioner at the same time.

5. The appointment information is only stored in a list while the program
   is running, so the information is not permanently saved.

### Part C - Use AI as Tutor: AI ON

#### AI Prompt

Act as a Python tutor.

I am learning introductory software technology.

Here is a small appointment-booking function.

1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

#### AI Tutor Response Summary

The AI helped me understand that the function:

- Checks whether a patient name has been provided.
- Creates a dictionary containing the patient, practitioner and
  appointment time.
- Adds the appointment dictionary to the appointments list.

The AI also identified possible limitations, including:

1. The practitioner name is not validated.
2. The appointment time is not validated.
3. The function does not check for conflicting or duplicate appointments.

Possible improvements included adding more input validation and checking
for appointment conflicts before adding an appointment.

### Part D - Generate an Alternative: AI ON

#### AI Prompt

Create a simple beginner-friendly Python function that stores a patient
name, practitioner name and appointment time.

Do not use a database or GUI.
Keep the code simple and suitable for an introductory Python student.

appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

    return appointment

#### AI-Generated Contribution

The AI generated an alternative `add_appointment()` function.

The function:
- Accepts a patient name, practitioner name and appointment time.
- Stores the information in a dictionary.
- Adds the dictionary to the appointments list.
- Returns the newly created appointment.

The generated version does not use a database or GUI.

### Part F - Verify Behaviour

| Test | Result |
|---|---|
| Normal appointment | The appointment is successfully added to the list. |
| Blank patient name | A `ValueError` is raised because the patient name is empty. |
| Same practitioner and time | The appointment is still added. The current prototype does not detect double bookings. |
| `patient_name=None` and `appointment_time=None` | A `ValueError` is raised because `None` for the patient name fails the existing patient-name check. The appointment-time value is not reached or separately validated in this test. |

### Part G - Improve One Thing

I chose to improve the validation of the practitioner name.

The original function checked whether the patient name was empty, but it
did not check the practitioner name.

I added:

`if not practitioner_name:`

`raise ValueError("Practitioner name cannot be empty")`

This prevents an appointment from being added when the practitioner name
is missing.

