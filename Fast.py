from fastapi import FastAPI
from src.Employee import Employee

app = FastAPI()

@app.get('/', tags=['users'])
def read_root():
    return {
        'Hello': 'World'
    }

@app.get('/items/{item_id}', tags=['users'])
def read_items(item_id: int):
    return {
        'item_id': item_id
    }

@app.get('/profiles', tags=['profiles'])
def read_profiles():
    return {
        'profiles': [
            'Admin',
            'Reporter'
        ]
    }

@app.post('/users', tags=['users'])
def set_user(employee: Employee):
    return {
        'error': True,
        'data': employee
    }