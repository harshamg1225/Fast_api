from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address


address_dict = {"city": "kol", "state": "kar", "pin": "571440"}
address1 = Address(**address_dict)


Patient_detail = {"name": "Harsha", "age": 34, "gender": "Male", "address": address1}

patient_info = Patient(**Patient_detail)

print(patient_info.address.state)
