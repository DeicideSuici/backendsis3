from pydantic import BaseModel, ValidationError, validator, conint, confloat, EmailStr, Extra, constr, Field
from typing import List
from enum import Enum
import bcrypt

class RolMenu(str, Enum):
    admin = 'ADMIN'
    blogger = 'BLOGGER'
    user = 'USERNAME'

class Employee(BaseModel):
    employee_id: int = Field(None, alias='id')
    name: constr(strip_whitespace=True, strict=True, min_length=2, curtail_length=25)
    first_name: str
    last_name: str
    age: conint(gt=18, lt=30)
    email: EmailStr
    password: str
    hash_tag: constr(min_length=5, strip_whitespace=True) | None
    menu: List[str]
    rol: RolMenu

    class Config:
        extra = Extra.ignore

    @validator('hash_tag')
    def validate_hash_tag(cls, value):
        if not value.startswith('#'):
            raise ValueError('Hash Tag Must Start With (#)')
        return value.lower()
    
    @validator('first_name')
    def validate_first_name(cls, value):
        if len(value) < 5:
            raise ValueError('(5) Characters Mininum')
        return value
    
    def encrypt_password(self):
        encode = self.password.encode('utf-8')
        self.password = bcrypt.hashpw(encode,bcrypt.gensalt()).decode()

# employee_data_1 = {
#     'id': 1,
#     'name': 'Eduardo',
#     'first_name': 'Ramirez',
#     'last_name': 'Navarro',
#     'age': 21,
#     'email': 'eduardo@gmail.com',
#     'hash_tag': '#ElEdwin2023'
# }

# employee_data_2 = {
#     'id': 2,
#     'name': 'Mariana',
#     'first_name': 'Olalde',
#     'last_name': 'Rangel',
#     'age': 22,
#     'email': 'mariana@gmail.com',
#     'someone': 'extra',
#     'hash_tag': '#ElEdwin2023'
# }

# try:
#     employee_1 = Employee(**employee_data_1)
#     employee_2 = Employee(**employee_data_2)
#     print('#' * 100)
#     print(employee_1.json())
#     print('#' * 100)
#     print(employee_2.json())
#     print('#' * 100)
# except ValidationError as VE:
#     print('[ Pydantic Error ]')
#     print(VE)