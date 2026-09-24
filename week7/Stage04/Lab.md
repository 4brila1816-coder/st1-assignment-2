# Stage 4 Lab Activities
## Implementing the SmartCare Domain Layer

### Part A - Revisit Approved UML

The approved SmartCare domain model contains three main domain classes:
Patient, Practitioner and Appointment.

#### Patient
Responsibilities:
- Store patient information.
- Provide patient information when required.
- Be associated with appointments.

#### Practitioner
Responsibilities:
- Store practitioner information.
- Provide practitioner information when required.
- Be associated with appointments.
- Provide practitioner availability information.

#### Appointment
Responsibilities:
- Store appointment information.
- Associate a Patient with a Practitioner.
- Record the current appointment status.
- Support appointment cancellation.
- Maintain appointment information for appointment history.

#### Relationships
- A Patient can be associated with multiple Appointments.
- Each Appointment is associated with one Patient.
- A Practitioner can be associated with multiple Appointments.
- Each Appointment is associated with one Practitioner.
- Appointment uses association rather than inheritance with Patient and Practitioner.

### Part B - Implement Patient: AI OFF

The Patient class was implemented without AI assistance.

The implementation includes:
- A type hint for the patient name.
- Basic validation of the patient name.
- A ValueError if the supplied name is not a valid non-empty string.

The Patient class remains focused on patient information and does not
include database, UI or appointment-management logic.

### Part C - Implement Practitioner: AI OFF

The Practitioner class was implemented without AI assistance.

The implementation includes:
- An identifier.
- A practitioner name.
- A specialty.
- Type hints for each value.
- Basic validation to prevent invalid or empty values.

No database logic was included in the Practitioner class.

### Part D - Implement Appointment: AI ON

#### AI Prompt

Act as a Python pair programmer. Implement only the Appointment class
from the approved SmartCare UML.

Use type hints and an AppointmentStatus enum.

Cancelled appointments must remain as objects.

Do not add database, UI, notification or service classes.

Protect status transitions and explain any decision not directly visible
in the UML.

#### AI-Generated Contribution

AI generated:
- An AppointmentStatus enum containing SCHEDULED and CANCELLED.
- Type hints for the Appointment class.
- References to Patient and Practitioner.
- A protected _status attribute.
- A status property for reading the current status.
- A cancel() method that controls the status transition.
- A ValueError when cancellation is attempted on an already cancelled
  appointment.

The generated implementation did not add database, UI, notification or
service classes.

### Part E - Review Generated Code

| Review Area | Finding | Decision |
|---|---|---|
| Model consistency | The code contains Patient, Practitioner, appointment time, status and cancellation behaviour from the approved design. | Accept |
| Unsupported features | No database, UI, notification or service functionality was added. | Accept |
| Public state mutation | Status is stored as _status and can be read through the status property rather than changed directly. | Accept |
| Unnecessary inheritance | Appointment does not inherit from Patient, Practitioner or another unrelated class. | Accept |
| Invented dependencies | No NotificationManager, database or other unsupported dependency was introduced. | Accept |
| Error handling | Repeated cancellation raises a ValueError instead of silently allowing an illegal repeated transition. | Accept |

#### Review Decision

The AI-generated Appointment implementation was reviewed against the
approved design and the constraints provided in the AI prompt.

The implementation keeps Appointment associated with Patient and
Practitioner rather than using inheritance. Status is protected and changed
through the cancel() operation rather than being publicly modified.

No database, UI, notification or service classes were introduced.

The repeated cancellation check was kept because it protects the
Appointment status transition and allows an illegal repeated transition
to be detected during manual behaviour testing.

### Part F - Manual Behaviour Checks

| Test | Expected Result | Actual Result |
|---|---|---|
| Create valid Patient, Practitioner and Appointment | Objects are created successfully | Passed |
| Create Patient with an empty name | ValueError is raised | Passed |
| Cancel a SCHEDULED appointment | Status changes to CANCELLED | Passed |
| Cancel an already CANCELLED appointment | ValueError is raised | Passed |

The manual behaviour checks confirmed that valid domain objects could be
created and that basic validation worked correctly.

A scheduled appointment could be cancelled successfully. A second
cancellation attempt was rejected, showing that the Appointment class
protected the status transition.

### Part F - Manual Behaviour Checks

| Test | Expected Result | Actual Result |
|---|---|---|
| Create valid Patient, Practitioner and Appointment | Objects are created successfully | Passed |
| Create Patient with an empty name | ValueError is raised | Passed |
| Cancel a SCHEDULED appointment | Status changes to CANCELLED | Passed |
| Cancel an already CANCELLED appointment | ValueError is raised | Passed |

The manual behaviour checks confirmed that valid domain objects could be
created and that basic validation worked correctly.

A scheduled appointment could be cancelled successfully. A second
cancellation attempt was rejected, showing that the Appointment class
protected the status transition.

### Reflection

I did not need to reject a major part of the AI-generated Appointment
implementation because the prompt already placed clear constraints on what
the AI could generate. However, I still reviewed each part before accepting
it rather than assuming the generated code was correct.

The approved design constrained the AI by limiting the implementation to
the responsibilities of Appointment. The prompt specified that database,
UI, notification and service classes should not be added. It also required
the appointment status to be protected.

The protected status and cancel() method were kept because they allowed
Appointment to control its own status transition. I also verified the
repeated cancellation behaviour through manual testing.

This showed me that providing the approved design and clear constraints to
AI can reduce unnecessary features, but the generated code still needs to
be reviewed and verified.