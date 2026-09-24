class Practitioner:
    def __init__(self, identifier: str, name: str, specialty: str):
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError("Practitioner identifier must be a non-empty string.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Practitioner name must be a non-empty string.")

        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Practitioner specialty must be a non-empty string.")

        self.identifier = identifier
        self.name = name
        self.specialty = specialty