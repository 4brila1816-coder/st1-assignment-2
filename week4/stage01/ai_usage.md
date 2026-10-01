# Stage 1 AI Usage

## Part C - AI as Tutor

### Prompt

Act as a Python tutor.

I am learning introductory software technology.

Here is a small appointment-booking function.

1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

### AI Contribution

The AI helped explain how the appointment-booking function works.

It identified limitations including:
- The practitioner name was not validated.
- The appointment time was not validated.
- The program did not check for conflicting appointments.

It suggested adding input validation and checking for appointment conflicts.

### Decision

I used the AI suggestions to help identify limitations, but I did not
automatically add all of the suggested changes. The suggestions still
needed to be compared with the requirements and tested.


## Part D - AI-Generated Alternative

### Prompt

Create a simple beginner-friendly Python function that stores a patient
name, practitioner name and appointment time.

Do not use a database or GUI.
Keep the code simple and suitable for an introductory Python student.

### AI Contribution

The AI generated an alternative `add_appointment()` function that:
- Accepted the patient name, practitioner name and appointment time.
- Stored the information in a dictionary.
- Added the appointment to a list.
- Returned the newly created appointment.

### Evaluation

The generated function was simple and only used the required appointment
information. It did not add a database or GUI.

However, it did not include input validation or appointment conflict
checking. It also returned the appointment even though this was not
specifically required.

### Verification

I reviewed the generated code and compared it with the human-written
version and the SmartCare requirements.

I also tested the program using normal and unusual inputs rather than
assuming that the AI-generated output was correct.