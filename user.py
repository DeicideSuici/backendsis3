from pydantic import BaseModel, validator, conint
import re

class User(BaseModel):
    idUser: int | None
    name: str
    first_name: str
    last_name: str | None
    age: conint(gt=18, lt=30)
    email: str
    password: str

    @validator('name')
    def cheackLastName(cls, value):
        if len(value) < 3:
            raise ValueError('Tiene que ser mayor a 2 letras')
        return value
    
    # @validator('age')
    # def checkAge(cls, value):
    #      if value < 18 or value > 30:
    #           raise ValueError("Tienes que tener de 18 a 30 años")
    #      return value

    @validator('first_name')
    def checkFirstName(cls, value):
        if type(value) != str:
            raise ValueError("Sólo se admiten letras")
        return value
    
    @validator('password')
    def re_pwd(cls, pwd):
        regex = re.compile(r'^.{6,}$')
        if not regex.match(pwd):
            raise ValueError("La contraseña debe contener al menos 6 caracteres")
        return pwd
    
    @validator('email')
    def re_email(cls, email):
        regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if not regex.match(email):
            raise ValueError("Ingresa un correo valido")
        return email

ul = {
     "user_id": 1, 
     "name": "Eduardo", 
     "first_name":"Ramírez", 
     "last_name": "Navarro",
     "age": 21,
     "email": "eduardo@gmailcom",
     "password": "123456"
}

user1 = User(**ul) #Pase de multiples parametros de un diccionario

# print(type(ul))
print("Usuario", user1)