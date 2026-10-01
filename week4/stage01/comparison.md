# Human and AI Version Comparison

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes. The code is simple and uses basic lists, dictionaries and functions. | Yes. The AI version is also short and beginner-friendly. |
| Runs successfully? | Yes, after testing the code. | Yes, after testing the generated function. |
| Uses only required features? | Yes. It stores the patient name, practitioner name and appointment time. | Yes. It stores the same required information without adding a database or GUI. |
| Adds assumptions? | Some. It assumes appointment information can be stored in a list and that the patient name cannot be empty. | Some. It assumes the appointment should be returned after it is added to the list. |
| Handles errors? | Partly. It checks for an empty patient name, but does not validate the practitioner name, appointment time or appointment conflicts. | No. The generated alternative does not include input validation or conflict checking. |

## Comparison

Both versions are simple and easy to understand. The human-written version
includes basic validation for an empty patient name, while the AI-generated
alternative does not include validation.

The AI version also returns the newly created appointment, which was not
specifically required. This shows why AI-generated code needs to be reviewed
against the requirements before it is accepted.