# SmartCare v0.3 - Domain Model

## Requirement-to-Concept Trace

| Requirement | Concept | State/behaviour | Decision |
|---|---|---|---|
| FR-01, FR-05 | Patient | Stores patient information; information can be managed and located | Class |
| FR-02, FR-07 | Practitioner | Stores practitioner information and relates to practitioner availability | Class |
| FR-03, FR-04, FR-06, FR-08, FR-09 | Appointment | Stores appointment information and status; can be created and cancelled | Class |
| FR-01, FR-02 | Name | Information describing a patient or practitioner | Attribute |
| FR-06 | Status | Describes the current state of an appointment | Attribute of Appointment |
| FR-08 | Cancellation | Action performed on an appointment | Behaviour of Appointment |
| No specific supporting FR | Clinic | Possible domain concept, but its own state/behaviour is not established | Not selected as a class |
| No supporting FR | Database | Technical implementation concept | Not a domain class |

## CRC Cards

### Patient

Responsibilities:
- Store patient information.
- Provide patient information when required.
- Be associated with appointments.

Collaborators:
- Appointment


### Practitioner

Responsibilities:
- Store practitioner information.
- Provide practitioner information when required.
- Be associated with appointments.
- Provide practitioner availability information.

Collaborators:
- Appointment


### Appointment

Responsibilities:
- Store appointment information.
- Associate a patient with a practitioner.
- Record the current appointment status.
- Support appointment cancellation.
- Maintain appointment information for appointment history.

Collaborators:
- Patient
- Practitioner


### Optional Class

No optional class selected.

Reason:
The confirmed requirements currently support Patient, Practitioner and
Appointment as the main domain classes. There is not enough requirement
evidence to justify another domain class.

## UML Class Diagram


┌──────────────────────┐
│       Patient        │
├──────────────────────┤
│ name                 │
├──────────────────────┤
│                      │
└──────────────────────┘


┌──────────────────────┐
│     Practitioner     │
├──────────────────────┤
│ name                 │
├──────────────────────┤
│                      │
└──────────────────────┘


┌──────────────────────┐
│     Appointment      │
├──────────────────────┤
│ appointment_time     │
│ status               │
├──────────────────────┤
│ cancel()             │
└──────────────────────┘

Patient                         Appointment
┌──────────────┐               ┌──────────────┐
│              │  1       0..* │              │
│   Patient    │───────────────│ Appointment  │
│              │               │              │
└──────────────┘               └──────────────┘

Patient                         Appointment
┌──────────────┐               ┌──────────────┐
│              │  1       0..* │              │
│   Patient    │───────────────│ Appointment  │
│              │               │              │
└──────────────┘               └──────────────┘

┌────────────────────┐                 ┌────────────────────────┐
│      Patient       │                 │      Practitioner      │
├────────────────────┤                 ├────────────────────────┤
│ name               │                 │ name                   │
├────────────────────┤                 ├────────────────────────┤
│                    │                 │                        │
└─────────┬──────────┘                 └───────────┬────────────┘
          │ 1                                      │ 1
          │                                        │
          │ 0..*                                   │ 0..*
          │                                        │
          └───────────────┐     ┌──────────────────┘
                          │     │
                  ┌───────┴─────┴────────┐
                  │     Appointment      │
                  ├──────────────────────┤
                  │ appointment_time     │
                  │ status               │
                  ├──────────────────────┤
                  │ cancel()             │
                  └──────────────────────┘

### Design Rationale

Patient, Practitioner and Appointment were selected as the main domain
classes because they are directly supported by the SmartCare requirements.

Appointment connects Patient and Practitioner because an appointment
represents a patient being scheduled with a practitioner.

A Patient can be associated with multiple appointments, while each
appointment is associated with one patient. A Practitioner can also be
associated with multiple appointments, while each appointment is associated
with one practitioner.

Status is represented as an attribute of Appointment rather than a separate
class because the current requirements only require the system to record and
display the current appointment status.

Cancellation is represented as behaviour of Appointment rather than a
separate class because cancellation is an action performed on an appointment.

Additional classes have not been added because they are not currently
supported by sufficient requirement evidence.

## AI Design Review Record

| AI Suggestion | Evidence | Decision | Reason | Model Change |
|---|---|---|---|---|
| Keep Patient, Practitioner and Appointment as the main domain classes | FR-01, FR-02, FR-03, FR-05 | Accepted | These concepts are directly supported by the confirmed requirements. | No change required. |
| Consider practitioner availability as a separate domain concept | FR-07 | Modified | Availability is supported, but there is not enough evidence to justify a separate class. | Availability remains associated with Practitioner. |
| Add NotificationManager | No supporting requirement | Rejected | Notifications are not part of the confirmed SmartCare requirements. | No class added. |
| Keep Status as part of Appointment | FR-06 | Accepted | The requirement supports appointment status but does not justify a separate Status class. | Status remains an Appointment attribute. |
| Add ScheduleEngine | FR-07 only supports availability | Rejected | The requirement supports viewing practitioner availability but does not confirm the need for a scheduling engine. | No ScheduleEngine added. |

## Part G - Python Skeletons

Python class skeletons were created for:

- Patient
- Practitioner
- Appointment

The class skeletons were based on the final domain model.

Only basic state and method structure were created. Full behaviour has not
been implemented at this stage.

## Part H - Consistency Check

### Model-Code Consistency
| UML Element | Python Code | Consistent? | Explanation |
|---|---|---|---|
| Patient class | Patient class in patient.py | Yes | Both represent a Patient as a domain class. |
| Patient.name | self.name | Yes | The UML attribute is represented in the Python class. |
| Practitioner class | Practitioner class in practitioner.py | Yes | Both represent a Practitioner as a domain class. |
| Practitioner.name | self.name | Yes | The UML attribute is represented in the Python class. |
| Appointment class | Appointment class in appointment.py | Yes | Both represent an Appointment as a domain class. |
| Appointment.appointment_time | self.appointment_time | Yes | Appointment time is represented in both. |
| Appointment.status | self.status | Yes | Appointment status is represented in both. |
| Patient-Appointment association | self.patient | Yes | Appointment contains a reference to a Patient. |
| Practitioner-Appointment association | self.practitioner | Yes | Appointment contains a reference to a Practitioner. |
| Appointment.cancel() | cancel() | Yes | Cancellation appears as Appointment behaviour in both. |

### Multiplicity Check

The UML model shows that a Patient may be associated with multiple
Appointments and a Practitioner may be associated with multiple Appointments.

The current Python skeleton stores a Patient and Practitioner reference
inside each Appointment. The reverse collection of appointments is not
implemented in Patient or Practitioner.

This is acceptable at the skeleton stage because full behaviour and
implementation are not required yet.

### Over-Design Check

The Python skeletons do not introduce additional classes such as
PatientManager, PractitionerManager, AppointmentManager, ClinicController,
NotificationManager or ScheduleEngine.

These classes were not included because there was insufficient confirmed
requirement evidence to support them in the final domain model.

### Consistency Result

The SmartCare v0.3 UML model and Python class skeletons are consistent at
the current stage.

Patient, Practitioner and Appointment appear in both the model and code.
The main attributes and Appointment cancellation operation are also
represented.

The Python code remains a skeleton and does not implement full system
behaviour. Further implementation should only be added when supported by
confirmed requirements.
