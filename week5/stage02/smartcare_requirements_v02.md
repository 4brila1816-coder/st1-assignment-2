# SmartCare v0.2 - Requirements Specification

## 1. Problem and Scope

SmartCare currently uses spreadsheets and paper records to manage clinic
information. Staff have reported duplicate bookings, difficulty finding
patient information, inconsistent appointment status and limited appointment
history.

Management wants a small, maintainable system for managing patients,
practitioners and appointments.

### In Scope

- Patient information management.
- Practitioner information management.
- Appointment information management.
- Addressing duplicate bookings.
- Addressing difficulty finding patient information.
- Managing appointment status consistently.
- Maintaining appointment history.
- Keeping the system small and maintainable.

### Out of Scope

Based on the current requirements evidence, the following are outside the
defined scope:

- Facial recognition login.
- Online payments.
- AI treatment recommendations.

### Provisional / Requires Validation

The following have not been confirmed by the client and require further
clarification:

- How patient information should be searched or located.
- What conditions make an appointment a duplicate booking.
- Which appointment status values are required.
- Which records should be retained in appointment history.
- Specific user roles and permissions.

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Clinic staff | A more consistent way to manage patient and appointment information. | Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. |
| Clinic management | A small, maintainable system for managing patients, practitioners and appointments. | Directly stated in the client brief. |
| Patients | Their patient and appointment information to be managed by the clinic system. | Patients are part of the system domain, but their specific needs are not directly stated in the client brief. This is provisional. |
| Practitioners | Their practitioner and appointment information to be managed by the clinic system. | Practitioners are part of the system domain, but their specific needs are not directly stated in the client brief. This is provisional. |

## 3. Functional Requirements

FR-01: The system shall allow patient information to be recorded.

FR-02: The system shall allow stored patient information to be viewed.

FR-03: The system shall allow practitioner information to be recorded.

FR-04: The system shall allow stored practitioner information to be viewed.

FR-05: The system shall allow appointment information to be recorded.

FR-06: The system shall allow stored appointment information to be viewed.

FR-07: The system shall detect duplicate appointment bookings.

FR-08: The system shall record the status of an appointment.

FR-09: The system shall allow appointment status to be viewed.

FR-10: The system shall retain appointment information so that appointment
history can be viewed.

## 4. Non-Functional Requirements

NFR-01: The system should be maintainable so that changes can be made without
unnecessarily affecting unrelated parts of the system.

NFR-02: The system should reliably preserve patient, practitioner and
appointment information.

NFR-03: The system should maintain the integrity of stored patient,
practitioner and appointment data.

NFR-04: Core business logic should be independently testable.

NFR-05: The system should provide clear and understandable interactions for
its intended users.

## 5. User Stories

US-01: As a clinic staff member, I want to view stored patient information,
so that I can find the patient information I need.

US-02: As a clinic staff member, I want to record appointment information,
so that appointments can be managed by the system.

US-03: As a clinic staff member, I want duplicate appointment bookings to be
detected, so that duplicate bookings can be identified.

US-04: As a clinic staff member, I want appointment status to be recorded,
so that appointment status can be managed consistently.

US-05: As a clinic staff member, I want to view appointment history,
so that previous appointment information can be found.

## 6. Acceptance Criteria

### AC-01 - View Patient Information

GIVEN a patient has been recorded in the system,

WHEN the staff member views the patient information,

THEN the system displays the stored patient information.


### AC-02 - Record Appointment Information

GIVEN the required appointment information is available,

WHEN the staff member records the appointment,

THEN the system stores the appointment information.


### AC-03 - Duplicate Booking - Failure Scenario

GIVEN the appointment would duplicate an existing booking,

WHEN the staff member attempts to record the appointment,

THEN the system detects the duplicate booking.

## 7. Assumptions and Open Questions

### Assumptions

- Clinic staff will interact with the system to manage clinic information.
- Patients and practitioners are part of the information managed by the system.
- The exact details of some system functions will require further clarification
  from the client.

### Open Questions

1. How should staff locate or search for patient information?

2. What conditions make an appointment a duplicate booking?

3. What appointment status values should the system support?

4. Which appointment records should be retained in appointment history?

5. Which user roles are allowed to record or manage appointments?

6. What information needs to be stored for each patient?

7. What information needs to be stored for each practitioner?

8. What information needs to be stored for each appointment?

9. How should system maintainability be measured?

10. Are specific reliability requirements or targets required?

11. How should system usability be measured?

## 8. AI Requirements Review Record

| AI Suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Clarify how patient information should be located. | Partial | Unverified | The client confirms difficulty finding patient information but does not specify a search method. | Requires client clarification. |
| Define what makes an appointment a duplicate booking. | Partial | Unverified | Duplicate bookings are a confirmed problem, but the conditions that define a duplicate are not provided. | Requires client clarification. |
| Define the required appointment status values. | Partial | Unverified | Inconsistent appointment status is a confirmed problem, but specific status values are not provided. | Requires client clarification. |
| Clarify which appointment records should remain in appointment history. | Partial | Unverified | Limited appointment history is a confirmed problem, but the required contents of the history are not specified. | Requires client clarification. |
| Make the maintainability requirement more measurable. | Yes | Accepted | Management specifically requests a maintainable system, but no measurement criteria are provided. | Maintainability is supported by the client brief; measurement criteria still require clarification. |
| Define measurable reliability criteria. | No specific target | Unverified | Reliability is an appropriate non-functional quality, but the client has not provided a reliability target. | Requires client clarification. |
| Define measurable usability criteria. | No specific target | Unverified | Usability is an appropriate non-functional quality, but the client has not provided measurable criteria. | Requires client clarification. |
| Confirm which user role records appointments. | Partial | Unverified | The brief refers to staff but does not define specific roles or permissions. | Requires client clarification. |

