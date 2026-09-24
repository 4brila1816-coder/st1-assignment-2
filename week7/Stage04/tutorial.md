# Stage 4 Tutorial Activities

## Object-Oriented Design Decisions

### Activity 1 - Encapsulation Review

| Class | Protected state / invariant | Public operations |
|---|---|---|
| Patient | Patient information must remain valid. | Create/initialise a patient and access patient information. |
| Practitioner | Identifier, name and specialty must remain valid. | Create/initialise a practitioner and access practitioner information. |
| Appointment | Appointment status must follow valid status transitions. | Create/initialise an appointment and cancel an appointment. |

### Activity 2 - Composition or Inheritance?

| Relationship | Decision | Reason |
|---|---|---|
| Appointment and Patient | Composition/association | An Appointment is associated with a Patient, but an Appointment is not a type of Patient. |
| Appointment and Practitioner | Composition/association | An Appointment is associated with a Practitioner, but an Appointment is not a type of Practitioner. |
| Doctor and Practitioner (hypothetical) | Inheritance | A Doctor could be a specialised type of Practitioner. |
| Clinic and Appointment | Composition/association | A Clinic may contain or manage appointments, but an Appointment is not a type of Clinic. |

### Activity 3 - Responsibility Allocation

**1. Who decides whether SCHEDULED can become CANCELLED?**

The Appointment class should decide whether SCHEDULED can become CANCELLED,
because the Appointment class is responsible for protecting its own status
transitions.

**2. Who validates a patient name?**

The Patient class should validate the patient name because it is responsible
for protecting its own state and ensuring its information is valid.

**3. Should Appointment execute SQL? Why?**

No. Appointment should not execute SQL because database logic is not a
responsibility of the domain class. Appointment should focus on appointment
state and behaviour.

**4. Should the UI decide whether a status transition is legal?**

No. The Appointment class should decide whether a status transition is legal.
This keeps the business rule inside the domain object instead of relying on
the UI to enforce it.

### Activity 4 - AI Code Critique

| Design problem | Correction |
|---|---|
| Appointment status can be changed publicly. | Protect the status so it can only be changed through valid Appointment operations. |
| SQL is included inside cancel(). | Remove SQL from Appointment because database logic should not be handled by the domain class. |
| Appointment depends on NotificationManager. | Remove the NotificationManager dependency because notifications are not part of the approved domain design. |
| Appointment inherits from PatientRecord. | Remove the inheritance because an Appointment is not a type of PatientRecord. Use the approved association with Patient instead. |
| Status transitions are not protected. | Appointment should control whether a status change is valid, such as SCHEDULED to CANCELLED. |

### Exit Question

Code can use object-oriented features such as classes, objects and methods
but still have poor object-oriented design if responsibilities are placed
in the wrong classes or the classes are unnecessarily dependent on each
other.

For example, an Appointment class could contain SQL, notification logic and
allow its status to be changed directly. The code would still use classes,
but the Appointment class would be responsible for things outside its domain
responsibilities and would not properly protect its own state.