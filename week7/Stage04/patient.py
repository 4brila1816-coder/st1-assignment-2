class Patient:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name must be a non-empty string.")

        self.name = name