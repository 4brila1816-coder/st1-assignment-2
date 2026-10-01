# Stage 2 Lab
## SmartCare Requirements Engineering

### Part A - Client Brief: AI OFF

SmartCare currently uses spreadsheets and paper records.

The problems identified by staff are:

- Duplicate bookings.
- Difficulty finding patient information.
- Inconsistent appointment status.
- Limited appointment history.

Management wants a small, maintainable system for managing:

- Patients
- Practitioners
- Appointments

### Part B - Stakeholders and Scope: AI OFF

#### Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Clinic staff | Manage patient and appointment information more effectively. | Staff currently report problems with duplicate bookings, finding patient information, appointment status and appointment history. |
| Practitioners | Have practitioner information managed within the system. | Management wants a system that manages practitioners. |
| Patients | Have their patient and appointment information managed by the clinic system. | Management wants a patient and appointment management system. |
| Clinic management | Have a small and maintainable system for managing patients, practitioners and appointments. | This is directly stated in the client brief. |

#### In Scope

- Managing patient information.
- Managing practitioner information.
- Managing appointment information.
- Addressing duplicate bookings.
- Addressing difficulty finding patient information.
- Managing appointment status consistently.
- Maintaining appointment history.
- Keeping the system small and maintainable.

#### Provisional - Requires Validation

The following features may relate to the identified problems, but are not
confirmed by the current client brief:

- Searching for patients by a specific identifier.
- Cancelling appointments.
- Retaining cancelled appointments in appointment history.
- Practitioners viewing their schedules.
- Specific staff roles and permissions.

#### Out of Scope

The following features are not supported by the current client brief:

- Facial recognition login.
- Online payments.
- AI treatment recommendations.

### Part C - Functional Requirements: AI OFF

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

### Part D - Non-Functional Requirements: AI OFF

NFR-01: The system should be maintainable so that changes can be made without
unnecessarily affecting unrelated parts of the system.

NFR-02: The system should reliably preserve patient, practitioner and
appointment information.

NFR-03: The system should maintain the integrity of stored patient,
practitioner and appointment data.

NFR-04: Core business logic should be independently testable.

NFR-05: The system should provide clear and understandable interactions for
its intended users.

### Part E - User Stories and Acceptance Criteria: AI OFF

#### US-01 - Patient Information

As a clinic staff member,
I want to view stored patient information,
so that I can find the patient information I need.

**Acceptance Criteria**

GIVEN a patient has been recorded in the system,
WHEN the staff member views the patient information,
THEN the system displays the stored patient information.


#### US-02 - Appointment Recording

As a clinic staff member,
I want to record appointment information,
so that appointments can be managed by the system.

**Acceptance Criteria**

GIVEN the required appointment information is available,
WHEN the staff member records the appointment,
THEN the system stores the appointment information.


#### US-03 - Duplicate Bookings

As a clinic staff member,
I want duplicate appointment bookings to be detected,
so that duplicate bookings can be identified.

**Acceptance Criteria - Successful Scenario**

GIVEN the appointment does not duplicate an existing booking,
WHEN the staff member records the appointment,
THEN the system stores the appointment.

**Acceptance Criteria - Failure Scenario**

GIVEN the appointment would duplicate an existing booking,
WHEN the staff member attempts to record the appointment,
THEN the system detects the duplicate booking.


#### US-04 - Appointment Status

As a clinic staff member,
I want appointment status to be recorded,
so that appointment status can be managed consistently.

**Acceptance Criteria**

GIVEN an appointment exists,
WHEN its status is recorded,
THEN the system stores the appointment status.


#### US-05 - Appointment History

As a clinic staff member,
I want to view appointment history,
so that previous appointment information can be found.

**Acceptance Criteria**

GIVEN appointment information has previously been stored,
WHEN the staff member views the appointment history,
THEN the system displays the retained appointment information.

### Part F - AI Requirements Review: AI ON

#### Prompt Used

"Act as a software requirements reviewer. Review the SmartCare requirements
for ambiguity, inconsistency, missing clarification questions and testability.
Do NOT invent new client requirements. For every suggestion, state whether it
is based on evidence or is only a question/assumption requiring validation."

#### AI Review

| Requirement | AI Review / Suggestion | Evidence or Validation Needed |
|---|---|---|
| FR-02 | "Viewed" is clear as a general capability, but the method for finding a patient is not defined. Clarify how patient information should be located. | Question requiring validation. The client reports difficulty finding patient information but does not specify a search method. |
| FR-07 | "Duplicate appointment booking" is ambiguous because the conditions that make two bookings duplicates are not defined. | Question requiring validation. Duplicate bookings are identified as a problem, but the client does not define a duplicate. |
| FR-08 | The possible appointment status values are not defined. Clarify which statuses the system should support. | Question requiring validation. Inconsistent appointment status is identified as a problem, but specific statuses are not provided. |
| FR-10 | The requirement does not define which appointment records must remain in the history. | Question requiring validation. Limited appointment history is identified as a problem, but the required contents of the history are not specified. |
| NFR-01 | "Maintainable" is not measurable, so it may be difficult to objectively test. | Evidence supports maintainability, but measurable criteria require validation. |
| NFR-02 | "Reliably preserve" is vague because no reliability criteria are defined. | Question requiring validation. No specific reliability target is provided. |
| NFR-05 | "Clear and understandable" is subjective and is difficult to objectively test. | Question requiring validation. No measurable usability criteria are provided. |
| US-02 | The user story assumes that a clinic staff member records appointments. Confirm which user role is responsible for this action. | Assumption requiring validation. The brief refers to staff but does not define specific roles or permissions. |

### Part G - VERIFY the AI Review

| AI Suggestion | Decision | Reason / Evidence |
|---|---|---|
| Clarify how patient information should be located for FR-02. | Unverified | The client confirms that finding patient information is difficult, but does not specify how patients should be searched for or located. |
| Clarify what makes an appointment a duplicate for FR-07. | Unverified | Duplicate bookings are a confirmed problem, but the client does not define the conditions that make a booking a duplicate. |
| Define the appointment status values for FR-08. | Unverified | Inconsistent appointment status is a confirmed problem, but the client does not provide the required status values. |
| Clarify which appointment records should remain in history for FR-10. | Unverified | Limited appointment history is a confirmed problem, but the client does not specify which records must be retained. |
| Make NFR-01 more measurable. | Accepted | The client specifically requests a maintainable system, but the current requirement does not provide a measurable way to evaluate maintainability. |
| Define measurable reliability criteria for NFR-02. | Unverified | Reliability is an appropriate non-functional quality, but the client has not provided a specific reliability target. |
| Define measurable usability criteria for NFR-05. | Unverified | Usability is an appropriate non-functional quality, but the client has not provided measurable usability criteria. |
| Confirm which user role is responsible for recording appointments in US-02. | Unverified | The client brief refers to staff, but does not define specific roles or permissions for recording appointments. |

### Part H - Finalise SmartCare v0.2

The SmartCare v0.2 Requirements Specification will include the requirements
developed and reviewed during Stage 2.

The final specification will contain:

- Stakeholder analysis.
- In-scope and out-of-scope items.
- 10 functional requirements.
- 5 non-functional requirements.
- 5 user stories.
- Given-When-Then acceptance criteria.
- Assumptions and open questions.
- Selected evidence from the AI requirements review.

#### Assumptions and Open Questions to Carry Forward

The following items require further clarification from the client:

1. How should staff locate or search for patient information?
2. What conditions make an appointment a duplicate booking?
3. What appointment status values should the system support?
4. Which appointment records should remain in appointment history?
5. Which user roles are responsible for recording appointments?
6. How should maintainability be measured?
7. Are specific reliability measures required?
8. How should usability be measured?

#### Selected AI Review Evidence

The AI review identified ambiguity in the definition of duplicate bookings,
appointment statuses and appointment history.

It also identified that some non-functional requirements are difficult to
test because measurable criteria have not been provided.

These suggestions were checked against the client brief. Where the available
evidence was not enough to confirm a change, the issue was kept as an open
question rather than being added as a new client requirement.
