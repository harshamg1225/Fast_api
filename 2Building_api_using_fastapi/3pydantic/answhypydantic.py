from pydantic import BaseModel, EmailStr, AnyUrl, Field, StrictStr, StrictInt
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: StrictStr = Field(..., max_length=50)
    email: EmailStr
    linkedin_url: AnyUrl
    age: StrictInt = Field(
        ...,
        gt=0,
        title="age of the patient",
        description="this will take age of the patient that gretater than 0",
        examples=[23, 45],
    )

    weight: Annotated[int, Field(..., gt=0)]
    married: bool = False
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_detail: Dict[str, str]


patient_info = {
    "name": "harsha",
    "linkedin_url": "https://linkedin.com",
    "age": 20,
    "weight": 34,
    "allergies": ["pollen", "dust"],
    "contact_detail": {"phone_number": "9199102910"},
    "email": "abc@gmail.com",
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
