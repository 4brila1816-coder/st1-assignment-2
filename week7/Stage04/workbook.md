# SmartCare v0.4 - Domain Implementation Workbook

## 1. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
|---|---|---|---|
| Patient class | `Patient` class in `patient.py` | Yes | Implements the Patient domain object. |
| Patient name | `self.name` | Yes | Name is stored and basic validation is performed. |
| Practitioner class | `Practitioner` class in `practitioner.py` | Yes | Implements the Practitioner domain object. |
| Practitioner identifier | `self.identifier` | Yes | Stores the practitioner's identifier. |
| Practitioner name | `self.name` | Yes | Stores the practitioner's name. |
| Practitioner specialty | `self.specialty` | Yes | Stores the practitioner's specialty. |
| Appointment class | `Appointment` class in `appointment.py` | Yes | Implements the Appointment domain object. |
| Patient association | `self.patient` | Yes | Appointment holds a reference to a Patient. |
| Practitioner association | `self.practitioner` | Yes | Appointment holds a reference to a Practitioner. |
| Appointment time | `self.appointment_time` | Yes | Stores the appointment time. |
| Appointment status | `self._status` | Yes | Status is protected from direct modification. |
| Appointment cancellation | `cancel()` | Yes | Controls the transition from SCHEDULED to CANCELLED. |
| Appointment status values | `AppointmentStatus` | Yes | Enum defines SCHEDULED and CANCELLED states. |

## 2. Domain Invariants

| Class | Invariant / rule | How protected |
|---|---|---|
| Patient | Patient name must contain a valid non-empty value. | The constructor validates the name and raises a ValueError for invalid input. |
| Practitioner | Identifier, name and specialty must contain valid non-empty values. | The constructor validates the values before storing them. |
| Appointment | A new appointment begins with SCHEDULED status. | The constructor sets `_status` to `AppointmentStatus.SCHEDULED`. |
| Appointment | Appointment status should not be changed directly. | Status is stored in `_status` and exposed through a read-only `status` property. |
| Appointment | A SCHEDULED appointment can be changed to CANCELLED. | The `cancel()` method controls the status transition. |
| Appointment | A CANCELLED appointment cannot be cancelled again. | `cancel()` raises a `ValueError` when a repeated cancellation is attempted. |

## 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
|---|---|---|
| Appointment and Patient | Composition/association | An Appointment is associated with a Patient, but an Appointment is not a type of Patient. |
| Appointment and Practitioner | Composition/association | An Appointment is associated with a Practitioner, but an Appointment is not a type of Practitioner. |
| Doctor and Practitioner (hypothetical) | Inheritance | A Doctor could be a specialised type of Practitioner. |
| Clinic and Appointment | Composition/association | A Clinic may contain or manage appointments, but an Appointment is not a type of Clinic. |

## 4. AI Pair-Programming Record

| AI contribution | Conforms? | Decision | Reason | Verification |
|---|---|---|---|---|
| Created an AppointmentStatus enum with SCHEDULED and CANCELLED | Yes | Accepted | Provides controlled status values and follows the constraints given to AI. | Compared with the approved design and checked through manual testing. |
| Associated Appointment with Patient and Practitioner | Yes | Accepted | Matches the relationships in the approved domain model. | Compared with the UML model. |
| Used a protected `_status` attribute | Yes | Accepted | Prevents appointment status from being changed directly. | Reviewed the code and confirmed status changes through `cancel()`. |
| Added `cancel()` to change SCHEDULED to CANCELLED | Yes | Accepted | Cancellation is an agreed responsibility of Appointment. | Manual cancellation test confirmed the status changed to CANCELLED. |
| Added a `ValueError` for repeated cancellation | Yes | Accepted | Prevents an illegal repeated status transition. | Manual repeated-cancellation test raised a ValueError. |
| Did not add database, UI, notification or service classes | Yes | Accepted | These were explicitly excluded from the AI implementation. | Reviewed the generated code and its dependencies. |

## 5. Updated UML

The implementation revealed some justified changes and additional detail
that should be represented in the UML model.

### Changes

1. Practitioner now includes `identifier`, `name` and `specialty`, as
   required by the Stage 4 implementation.

2. Appointment status is represented using the `AppointmentStatus` enum.

3. Appointment controls its status through `cancel()` rather than allowing
   the status to be changed directly.

4. The relationships between Appointment, Patient and Practitioner remain
   unchanged.

┌─────────────────────────┐
│         Patient         │
├─────────────────────────┤
│ name: str               │
└────────────┬────────────┘
             │ 1
             │
             │ 0..*
             │
      ┌──────┴──────────────────────┐
      │         Appointment         │
      ├─────────────────────────────┤
      │ patient: Patient            │
      │ practitioner: Practitioner  │
      │ appointment_time: str       │
      │ _status: AppointmentStatus  │
      ├─────────────────────────────┤
      │ status                      │
      │ cancel(): None              │
      └──────┬──────────────────────┘
             │ 0..*
             │
             │ 1
┌────────────┴────────────┐
│      Practitioner       │
├─────────────────────────┤
│ identifier: str         │
│ name: str               │
│ specialty: str          │
└─────────────────────────┘


┌─────────────────────────┐
│   <<enumeration>>       │
│   AppointmentStatus     │
├─────────────────────────┤
│ SCHEDULED               │
│ CANCELLED               │
└─────────────────────────┘


