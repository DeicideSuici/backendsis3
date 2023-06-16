from src.Employee import Employee

employee_data = {
    "id": 1, 
    "name": "Eduardo", 
    "first_name":"Ramírez", 
    "last_name": "Navarro",
    "age": 21,
    "email": "eduardo@gmail.com",
    "password": "123456",
    "hash_tag": "#BackendSis3",
    "menu": [
        "Home",
        "Marketplace"
        "My Profile"
        "Administrator"
        "About Us"
    ],
    "rol": "ADMIN"
}

employee = Employee(**employee_data)
employee.encrypt_password()

print('-' * 100)

for field, value in employee.__dict__.items():
    print('{}: {}'.format(field, value))

print('-' * 100)