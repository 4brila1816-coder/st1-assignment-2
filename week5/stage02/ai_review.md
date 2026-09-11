# SmartCare Stage 2 - AI Requirements Review

## Part F - AI Requirements Review

### AI Prompt

Act as a software requirements reviewer. Review the SmartCare requirements
for ambiguity, inconsistency, missing clarification questions and testability.
Do NOT invent new client requirements. For every suggestion, state whether
it is based on evidence or is only a question/assumption requiring validation.
### AI Review Results
1. FR-01 and FR-02 use the phrase "create and maintain", which is unclear.

Evidence:
The client confirmed that the system should support patient and practitioner
management.

Issue:
The word "maintain" does not explain whether users can view, edit, update or
delete information.

Suggestion:
Clarify what actions are included in patient and practitioner management.

Classification:
Question requiring validation.


2. FR-04 states that the system shall prevent duplicate appointment bookings.

Evidence:
Duplicate appointment bookings are specifically identified as a current
problem.

Issue:
The requirement does not define what counts as a duplicate booking.

Suggestion:
Clarify whether a duplicate means the same practitioner, same patient,
same date/time, or a combination of these.

Classification:
Evidence-based clarification required.


3. FR-06 requires the system to record and display appointment status.

Evidence:
Inconsistent appointment status information is identified as a current problem.

Issue:
The allowed appointment statuses have not been defined.

Suggestion:
Ask the client which appointment statuses are required.

Classification:
Evidence-based clarification required.


4. FR-07 requires the system to display practitioner availability.

Evidence:
Limited visibility of practitioner availability is identified as a current
problem.

Issue:
The requirement does not explain how availability is recorded or displayed.

Suggestion:
Clarify how practitioner availability should be represented.

Classification:
Evidence-based clarification required.


5. FR-08 states that appointments can be cancelled.

Evidence:
The case study identifies manual cancellation processes as a current problem.

Issue:
The system requirements do not define what should happen after an appointment
is cancelled.

Suggestion:
Clarify whether cancelled appointments remain visible in appointment history
and what status should be recorded.

Classification:
Evidence-based clarification required.


6. FR-10 states that the system shall produce basic operational reports.

Evidence:
The case study identifies difficulty producing basic operational reports.

Issue:
The specific reports required by management have not been identified.

Suggestion:
Ask management which reports are required in the first version.

Classification:
Evidence-based clarification required.


7. NFR-01 uses the word "reliably".

Issue:
"Reliably" is not measurable and could be interpreted in different ways.

Suggestion:
Ask the client whether a measurable reliability target is required.

Classification:
Question requiring validation.


8. NFR-03 states that the system should be "simple and understandable".

Issue:
These terms are subjective and difficult to test.

Suggestion:
Define measurable usability criteria after receiving more information from
the client.

Classification:
Question requiring validation.


9. NFR-04 states that the system shall maintain consistent information.

Evidence:
The case study identifies inconsistent appointment status information and
unreliable appointment history.

Issue:
The requirement does not explain what consistency checks are required.

Suggestion:
Clarify which data rules must be enforced.

Classification:
Evidence-based clarification required.


10. US-02 only describes a successful patient search.

Issue:
The acceptance criteria do not describe what should happen if the patient
cannot be found.

Suggestion:
Add a negative scenario after confirming the expected behaviour with the client.

Classification:
Question requiring validation.

## Part G - Verification
## Part G - Verification of AI Review

### 1. Clarify "create and maintain" in FR-01 and FR-02
Decision: Accepted

Reason:
The case study confirms that patient and practitioner management are required,
but it does not explain exactly what "maintain" includes.

Evidence:
The client states that the system should support patient and practitioner
management.

Action:
Keep this as an open clarification question.

### 2. Define duplicate appointment booking
Decision: Accepted

Reason:
Duplicate appointment bookings are specifically identified as a current
problem, but the client has not defined exactly what makes two appointments
duplicates.

Action:
Keep this as an open clarification question.

### 3. Define appointment statuses
Decision: Accepted

Reason:
The case study identifies inconsistent appointment status information as a
problem, but it does not list the allowed appointment statuses.

Action:
Ask the client which appointment statuses are required.
### 4. Clarify how practitioner availability is represented
Decision: Accepted

Reason:
The case study confirms that limited visibility of practitioner availability
is a problem, but it does not state how availability should be recorded or
displayed.

Action:
Keep this as an open clarification question.
### 5. Clarify what happens to cancelled appointments
Decision: Modified

Reason:
The case study confirms that manual cancellation is a current problem.
However, the AI suggestion that cancelled appointments should remain visible
in appointment history is not directly confirmed by the client.

Action:
Ask the client what should happen to an appointment after cancellation rather
than assuming that it must remain in history.
### 6. Define required operational reports
Decision: Accepted

Reason:
The case study confirms that producing basic operational reports is currently
difficult, but it does not identify which reports management needs.

Action:
Ask management which reports should be included in the first version.
### 7. Add a measurable reliability target
Decision: Unverified

Reason:
The Stage 2 activity asks us to consider reliability as a non-functional
quality, but the client has not provided a measurable reliability target.

Action:
Do not invent a percentage, uptime target or response-time value.
Ask the client if a measurable target is required.
### 8. Add measurable usability criteria
Decision: Unverified

Reason:
The case study says the first version should be manageable and suitable for a
small clinic, but it does not give a measurable usability requirement.

Action:
Do not invent a usability score or time limit.
Ask the client how usability should be evaluated.
### 9. Define data consistency rules
Decision: Modified

Reason:
The case study identifies inconsistent appointment status information and
unreliable appointment history, so data consistency is relevant.

However, the exact consistency rules are not provided.

Action:
Keep data integrity as a requirement, but record the detailed rules as an
open question rather than inventing them.
### 10. Add a failed patient-search scenario
Decision: Unverified

Reason:
The case study confirms that staff currently have difficulty locating patient
records, but it does not specify what the software should display if a patient
cannot be found.

Action:
Do not assume a specific error message.
Ask the client what should happen when no matching patient exists.

### Verification Summary

Accepted:
- Clarify patient and practitioner management actions
- Define duplicate booking rules
- Define appointment statuses
- Clarify practitioner availability
- Define required operational reports

Modified:
- Cancellation behaviour
- Data consistency rules

Unverified:
- Measurable reliability target
- Measurable usability criteria
- Failed patient-search behaviour

Rejected:
- None