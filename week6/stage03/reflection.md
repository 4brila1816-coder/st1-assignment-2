# Stage 3 Reflection

One of the hardest modelling decisions for me was deciding whether concepts
such as status, cancellation and practitioner availability should become
separate classes. At first, I thought that because they appeared in the
requirements they could each become their own class. After comparing them
with the requirements, I decided that status could remain an attribute of
Appointment and cancellation could be behaviour of Appointment. There was
also not enough information about practitioner availability to justify
creating another class for it.

AI was useful for reviewing the model and suggesting different ways the
classes could be organised. However, some suggestions could have made the
system more complicated than required. For example, classes such as
NotificationManager and ScheduleEngine would add more structure, but there
was not enough confirmed requirement evidence to support them. I therefore
rejected these suggestions rather than adding them just because AI proposed
them.

My final choices were mainly supported by the SmartCare v0.2 requirements.
Patient, Practitioner and Appointment were kept as the main classes because
they were directly connected to the confirmed system requirements. This
helped me keep the UML model and Python skeletons consistent without adding
functionality that had not been confirmed.