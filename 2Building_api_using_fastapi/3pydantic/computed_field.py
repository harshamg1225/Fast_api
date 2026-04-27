from pydantic import BaseModel, Field, EmailStr, computed_field, AnyUrl, model_validator
from typing import Dict, List, Annotated


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    email: EmailStr
    married: bool
    allegies: List[str]
    contact_detail: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:

        return self.weight // self.height**2


patient_info = {
    "name": "Harsha",
    "age": "30",
    "weight": 34,
    "height": 1.3,
    "married": True,
    "allegies": ["pollen", "dust"],
    "contact_detail": {"phone_number": "9199102910"},
    "email": "abc@hdfc.com",
}

patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allegies)
    print(patient.contact_detail)
    print(patient.email)
    print("inserted")


insert_patient_data(patient1)
