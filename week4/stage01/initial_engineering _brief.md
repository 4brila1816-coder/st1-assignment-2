# SmartCare v0.1 - Initial Engineering Brief

## 1. Problem Summary

SmartCare Community Clinic currently manages patient and appointment
information using spreadsheets and paper records. This system may make it
difficult for staff to efficiently manage and access information. The clinic
would like to develop software that can help manage patients, practitioners
and appointments in one system. The software should make it easier for staff
to record and access important information. However, the client's request is
currently very broad and does not provide enough detail to create a complete
solution. More information is needed from the client to understand the users
of the system, required features, data that needs to be stored and any
limitations.

## 2. Initial Stakeholders

| Stakeholder | Possible need |
|---|---|
| Clinic staff | An easy way to create, view and manage appointments. |
| Practitioners | To be able to view their appointments and patient information. |
| Patients | To have their appointment and personal information recorded correctly. |
| Clinic management | A reliable system for managing clinic information. |

## 3. Initial Features

| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Manage patients | Confirmed | The client specifically said the software needs to help manage patients. |
| Manage practitioners | Confirmed | The client specifically mentioned practitioners. |
| Book/cancel appointments | Provisional | This would be useful, but the client has not specifically requested these functions. |
| Search for patients | Provisional | It could make patient management easier, but it has not been confirmed by the client. |

## 4. Questions for the Client

1. What information needs to be stored about each patient and practitioner?

2. What information needs to be recorded for each appointment?

3. Should users be able to edit or cancel existing appointments?

4. Who will be allowed to access and use the system?

5. What should happen if two appointments are booked with the same
   practitioner at the same time?

## 5. What We Do Not Yet Know

1. We do not know exactly what patient and practitioner information needs
   to be stored.

2. We do not know what functions the different users need or who should
   have access to them.

3. We do not know what rules the system should follow when creating,
   changing or cancelling appointments.

# AI Activity Card - Ask, Check, Explain

## Before AI

### What do I think the code does? What problems can I already identify?

I think the code is used to create and display appointments for the
SmartCare clinic. It stores information about the patient, practitioner
and appointment time.

One problem I can already see is that the program may not check all of
the information that is entered. It may also allow two appointments to
be made with the same practitioner at the same time.

## AI Request

### Prompt

Act as a tutor. Explain this code and identify potential problems.
Do not provide a complete replacement. Ask me questions that help me
reason about the solution.

## Evaluate

| AI Suggestion | Evaluation | Reason |
|---|---|---|
| Check for blank patient names | Useful | A blank patient name could result in incomplete appointment information, so checking for it would improve the prototype. |

## Decide

| AI Suggestion | Decision | Reason |
|---|---|---|
| Check for blank patient names | Accept | A patient name is required for an appointment, and the Stage 1 prototype identifies a blank patient name as a possible problem. Adding this check prevents incomplete appointment information from being stored. |

## Verify

I verified the AI suggestion by:

- Running the code.
- Testing a normal appointment with a patient name.
- Testing an appointment with a blank patient name.
- Testing unusual input such as `patient_name=None`.
- Comparing the behaviour with the SmartCare requirements.

The blank patient name test raised a `ValueError`, showing that the
validation prevented an appointment with a missing patient name from
being added.

## Verify

I verified the AI suggestion by:

- Running the code.
- Testing a normal appointment with a patient name.
- Testing an appointment with a blank patient name.
- Testing unusual input such as `patient_name=None`.
- Comparing the behaviour with the SmartCare requirements.

The blank patient name test raised a `ValueError`, showing that the
validation prevented an appointment with a missing patient name from


## Explain

I can explain the final code without reading the AI response. I understand
that the program uses a list to store appointments and a dictionary to
store the patient name, practitioner name and appointment time for each
appointment.

I also understand that `book_appointment()` creates and stores an
appointment, while `display_appointments()` displays the appointments
that have been recorded.

I still need to understand more about how to properly validate appointment
times and how the program could detect conflicting appointments, such as
two appointments with the same practitioner at the same time.