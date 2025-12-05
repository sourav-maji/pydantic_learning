from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at : datetime
    address : Address
    tags : List[str]= []

    model_config = ConfigDict(
        json_encoders= { datetime:  lambda v : v.strftime("%d-%m-%Y %H:%M:%S") }
    )


# Create a user instance

user = User(
    id=1,
    name="Sourav",
    email="Sourav@sourav.com",
    created_at= datetime(2024,3,15,14,30),
    address= Address(
        street="Something 123",
        city="Jaipur",
        zip_code="10001"
    ),
    tags=["premium", "subscriber"]
)

# using model_dump() -> dict

python_dict = user.model_dump()
print(python_dict)


print("============\n")
# using model_dump_json()

json_str = user.model_dump_json()
print(json_str)