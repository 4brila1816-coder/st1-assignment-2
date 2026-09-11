# Part C — AI as Tutor  
**AI ON (Use only UC‑approved GenAI tools such as Microsoft Copilot)**

## Prompt Used
```
Act as a Python tutor.
I am learning introductory software technology.
Here is a small appointment‑booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.
```

---

## Example Code
```python
def book_appointment(name, time):
    print("Appointment booked for", name, "at", time)
```

---

## 1. Explanation of What the Code Does
The function `book_appointment()` takes two inputs — a **name** and an **appointment time** — and prints a confirmation message. It does not store the appointment or check whether the inputs are valid; it simply displays text to the user.

---

## 2. Three Limitations
1. **No data storage**  
   The appointment is not saved anywhere, so it cannot be retrieved later.

2. **No error handling**  
   Invalid or empty inputs still produce output without warnings.

3. **No conflict checking**  
   The function cannot detect overlapping or duplicate appointment times.

---

## 3. Suggested Improvements  
*(Without rewriting the whole application)*

- Add a **list or dictionary** to store multiple appointments.  
- Validate inputs (e.g., ensure time follows a proper format).  
- Add simple **conflict detection** to prevent double‑booking.

---

## 4. No Full Rewrite  
These improvements can be added gradually while keeping the original structure intact.

---

## 5. Questions to Test Understanding
1. Why is storing appointments in a list or dictionary more useful than printing them?  
2. What problems might occur if two users book the same time without conflict checking?


# Part D — Generate an Alternative  
**AI ON (Use only UC‑approved GenAI tools such as Microsoft Copilot)**

## Prompt Used
```
Create a simple beginner‑friendly Python function that stores 
patient name, practitioner name, and appointment time.
Do not use a database.
Do not use a GUI.
```

---

## AI‑Generated Beginner‑Friendly Python Function

```python
# A simple function to store appointment details in a dictionary.
# No database and no GUI are used.

def create_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    return appointment

# Example usage:
appt = create_appointment("Alice", "Dr Smith", "10:30 AM")
print(appt)
```

---

## Explanation  
This function creates a **Python dictionary** containing three pieces of information:

- **patient** — the patient’s name  
- **practitioner** — the practitioner’s name  
- **time** — the appointment time  

The dictionary is returned so it can be stored in a list, printed, or used later in the program.  
This keeps the solution simple and beginner‑friendly while following the rules:  
✔ No database  
✔ No GUI  
✔ Only basic Python structures  

---