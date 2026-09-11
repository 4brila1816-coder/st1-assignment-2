# SmartCare Requirements Specification

## Part A - Client Brief

## Part A - Client Brief

SmartCare is a small community clinic that currently manages patient
information and appointments using spreadsheets, paper records and
manual processes.

The current system has several operational problems, including duplicate
appointment bookings, difficulty locating patient records, inconsistent
appointment status information, limited visibility of practitioner
availability, manual cancellation processes, unreliable appointment
history and difficulty producing basic operational reports.

Management wants a simple software system that initially supports patient,
practitioner and appointment management. The first version should be
manageable and suitable for a small clinic rather than a complex hospital
information system.

## Part B - Stakeholders and Scope

### Stakeholders
1. Clinic Management
   - Responsible for overseeing the clinic and deciding what the system needs to support.
   - Interested in having a simple and maintainable system and improving clinic operations.

2. Clinic Staff / Reception Staff
   - Use the current spreadsheet, paper and manual processes.
   - Would likely use the system to manage patient information and appointments.

3. Healthcare Practitioners / GPs
   - Provide consultations at SmartCare.
   - Need appointment information and visibility of their availability.

4. Patients
   - Attend appointments at SmartCare.
   - Their personal information and appointment records are managed by the clinic.
### In Scope
- Patient management
- Practitioner management
- Appointment management
- Viewing practitioner availability
- Appointment cancellation
- Maintaining appointment history
- Producing basic operational reports
### Out of Scope
- A complex hospital information system
- Large-scale hospital functionality beyond the needs of a small community clinic
### Provisional / Unconfirmed Features
- Online patient booking
- SMS or email appointment reminders
- Medicare integration
- Online payments
- Electronic prescriptions
- Patient self-service accounts
## Part C - Functional Requirements
FR-01: The system shall allow staff to create and maintain patient information.

FR-02: The system shall allow staff to create and maintain practitioner information.

FR-03: The system shall allow staff to create appointments for patients with practitioners.

FR-04: The system shall prevent duplicate appointment bookings.

FR-05: The system shall allow staff to locate and view patient information.

FR-06: The system shall record and display the current status of an appointment.

FR-07: The system shall allow staff to view practitioner availability.

FR-08: The system shall allow appointments to be cancelled.

FR-09: The system shall maintain a history of appointments.

FR-10: The system shall allow basic operational reports to be produced.

## Part D - Non-Functional Requirements
NFR-01 - Reliability:
The system shall operate reliably when managing patient, practitioner and appointment information.

NFR-02 - Maintainability:
The system shall be designed so that it can be maintained and updated without unnecessary complexity.

NFR-03 - Usability:
The system shall provide a simple and understandable way for clinic staff to manage patients, practitioners and appointments.

NFR-04 - Data Integrity:
The system shall maintain consistent patient, practitioner and appointment information.

NFR-05 - Testability:
The system shall be designed so that its main functions can be tested to verify that they meet the specified requirements.

## Part E - User Stories and Acceptance Criteria
### US-01 - Create an Appointment

As a clinic staff member,
I want to create an appointment for a patient with a practitioner,
so that the patient's consultation can be scheduled.

Acceptance Criteria:

Given a patient and practitioner are available,
When the staff member creates an appointment,
Then the appointment should be recorded in the system.

Failure Scenario:

Given the practitioner already has an appointment at the selected time,
When the staff member attempts to create another appointment,
Then the system should prevent the duplicate booking.
### US-02 - Find Patient Information

As a clinic staff member,
I want to locate patient information,
so that I can access the patient's information when needed.

Acceptance Criteria:

Given patient information exists in the system,
When the staff member searches for the patient,
Then the system should display the patient's information.
### US-03 - View Practitioner Availability

As a clinic staff member,
I want to view practitioner availability,
so that I can determine when a practitioner is available for an appointment.

Acceptance Criteria:

Given practitioner information exists in the system,
When the staff member views the practitioner's availability,
Then the system should display their available appointment information.
### US-04 - Cancel an Appointment

As a clinic staff member,
I want to cancel an appointment,
so that the appointment status can be updated when the appointment is no longer required.
### US-05 - View Appointment History

As a clinic staff member,
I want to view appointment history,
so that I can access previous appointment information when required.
## Part F - AI Requirements Review


## Part G - Verify the AI Review


## Part H - Finalise SmartCare


## Reflection