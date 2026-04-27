from pydantic import BaseModel, Field, field_validator, EmailStr, AnyUrl
from typing import List, Dict, Annotated, Literal


class Patient(BaseModel):
    name: str = Field(..., max_length=50)
    age: int = Field(...)
    married: bool = Field(...)
    weight: float = Field(..., gt=0)
    email: EmailStr = Field(...)
    allergies: List[str] = Field(..., max_length=5)
    contact_detail: Dict[str, str] = Field(...)
    linkedin_url: AnyUrl

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        valid_domain = ["hdfc.com", "icici.com"]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain")
        return value

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):

        if 0 < value < 100:
            return value

        else:
            raise ValueError("Age shoulf not be negative")


patient_info = {
    "name": "Harsha",
    "linkedin_url": "https://linkedin.com",
    "age": "20",
    "weight": 34,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_detail": {"phone_number": "9199102910"},
    "email": "abc@hdfc.com",
}

patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_detail)
    print(patient.email)
    print(patient.linkedin_url)
    print("inserted")


insert_patient_data(patient1)
