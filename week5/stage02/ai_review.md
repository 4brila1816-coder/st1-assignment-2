# Stage 2 AI Requirements Review

## AI Review Prompt

Act as a software requirements reviewer. Review the SmartCare requirements
for ambiguity, inconsistency, missing clarification questions and testability.
Do NOT invent new client requirements. For every suggestion, state whether it
is based on evidence or is only a question/assumption requiring validation.


## AI Review

| Requirement | AI Suggestion | Evidence / Validation |
|---|---|---|
| FR-02 | Clarify how patient information should be located. | The client confirms difficulty finding patient information, but a specific search method is not provided. Requires validation. |
| FR-07 | Define what makes an appointment a duplicate booking. | Duplicate bookings are a confirmed problem, but the conditions that define a duplicate are not provided. Requires validation. |
| FR-08 | Define the required appointment status values. | Inconsistent appointment status is a confirmed problem, but specific status values are not provided. Requires validation. |
| FR-10 | Clarify which appointment records should remain in appointment history. | Limited appointment history is a confirmed problem, but the required contents of the history are not specified. Requires validation. |
| NFR-01 | Make the maintainability requirement more measurable. | Maintainability is supported by the client brief, but no measurement criteria are provided. |
| NFR-02 | Define measurable reliability criteria. | Reliability is an appropriate quality, but no specific reliability target is provided. Requires validation. |
| NFR-05 | Define measurable usability criteria. | Usability is an appropriate quality, but no measurable usability criteria are provided. Requires validation. |
| US-02 | Confirm which user role is responsible for recording appointments. | The brief refers to staff but does not define specific roles or permissions. Requires validation. |


## Verification of AI Review

| AI Suggestion | Decision | Reason |
|---|---|---|
| Clarify how patient information should be located. | Unverified | The client identifies difficulty finding patient information, but does not specify how it should be located. |
| Define what makes an appointment a duplicate booking. | Unverified | Duplicate bookings are identified as a problem, but the duplicate-booking rule is not defined. |
| Define the required appointment status values. | Unverified | Appointment status is identified as a problem, but the required status values are not provided. |
| Clarify which appointment records should remain in appointment history. | Unverified | Limited appointment history is identified as a problem, but the required records are not specified. |
| Make the maintainability requirement more measurable. | Accepted | Management specifically requests a maintainable system, although measurement criteria still require clarification. |
| Define measurable reliability criteria. | Unverified | No specific reliability target is provided by the client. |
| Define measurable usability criteria. | Unverified | No measurable usability criteria are provided by the client. |
| Confirm which user role records appointments. | Unverified | The brief refers to staff but does not define specific roles or permissions. |


## AI Review Conclusion

The AI review identified several areas where the requirements could be
clearer or more testable. However, suggestions that required information
not contained in the client brief were not automatically added to the
requirements.

Instead, these suggestions were marked as unverified and carried forward
as open questions where appropriate. This prevents AI-generated assumptions
from being treated as confirmed client requirements.