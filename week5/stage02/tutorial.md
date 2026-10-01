| Stakeholder | Need | Potential conflict |
|---|---|---|
| Clinic staff | An easier way to manage patient and appointment information. | Staff may need additional functions that could make the system more complex. |
| Practitioners | Their practitioner and appointment information to be managed by the system. | Their needs may differ from the needs of other clinic staff. |
| Patients | Their patient and appointment information to be recorded and managed correctly. | Their information needs to be available for clinic use while still being managed appropriately. |
| Clinic management | A small and maintainable system for managing patients, practitioners and appointments. | Keeping the system small and maintainable may conflict with requests for additional features. |

### Activity 2 - Functional or Non-Functional?

| Requirement | Classification | Reason |
|---|---|---|
| The system shall allow staff to cancel an appointment. | Functional | It describes an action that the system must allow staff to perform. |
| The system should remain responsive for the course-scale dataset. | Non-functional | It describes the expected performance of the system rather than a specific function. |
| The system shall retain cancelled appointments. | Functional | It describes what the system must do with cancelled appointment records. |
| Core business logic should be independently testable. | Non-functional | It describes the testability of the system rather than a specific function. |
| The system shall search for a patient by ID. | Functional | It describes a specific capability that the system must provide. |

### Activity 3 - Repair Ambiguous Requirements

#### 1. The system should be easy to use.

**Problem:** "Easy to use" is vague because it does not explain how usability will be measured.

**Clarification question:** What would make the system easy to use for the intended users?


#### 2. Patient search should be fast.

**Problem:** "Fast" is unclear because no expected response time is given.

**Clarification question:** How quickly should patient search results be displayed?


#### 3. The system should securely manage data.

**Problem:** "Securely" is vague because the required security measures are not specified.

**Clarification question:** What security measures or access restrictions are required for the data?


#### 4. Appointments should normally be easy to cancel.

**Problem:** "Normally" and "easy to cancel" are unclear and cannot be consistently measured or tested.

**Clarification question:** Who should be able to cancel an appointment, and under what conditions?

### Activity 4 - AI Requirements Audit

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders. | Unsupported | SMS reminders are not mentioned in the SmartCare client brief. |
| Facial recognition login. | Out of scope | Facial recognition is not part of the stated patient, practitioner and appointment management system. |
| Receptionists create appointments. | Assumption requiring validation | The brief refers to staff and appointment management, but it does not confirm that receptionists are responsible for creating appointments. |
| Online payment. | Out of scope | Payments are not included in the stated scope of the SmartCare system. |
| Practitioners view schedules. | Assumption requiring validation | Practitioners are part of the system, but the brief does not specifically state that they need to view schedules. |
| AI recommends treatments. | Out of scope | Treatment recommendations are not part of the stated patient, practitioner and appointment management system. |
| Cancelled appointments remain in history. | Assumption requiring validation | The brief identifies limited appointment history as a problem, but it does not specifically state that cancelled appointments must remain in the history. |

### Exit Question

"AI suggested it" is not sufficient evidence for a requirement because AI
can generate features or assumptions that the client has not requested.

Requirements should be supported by evidence from the client or stakeholders.
AI can help identify possible requirements, problems or questions, but its
suggestions still need to be checked and validated before they are treated
as confirmed requirements.