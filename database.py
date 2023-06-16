from sqlalchemy import create_engine, MetaData, text
from fastapi import FastAPI

engime = create_engine("mysql+pymysql://root:@localhost:3306/dbfastapi")

meta_data = MetaData()
meta_data_object = meta_data

meta_data_object.reflect(bind=engime)

users = meta_data.tables['tbl_users']
profiles = meta_data.tables['tbl_profiles']

connect = engime.connect()

result = connect.execute(users.select()).fetchall()
result1 = connect.execute(users.select().where(users.c.id == 1)).first()
stmt = text('SELECT * FROM vw_users')
result_view = connect.execute(stmt).fetchall()

# Crear servicio con FastAPI
app = FastAPI()

@app.get('/', tags=['users'])
def read_root():
    return {
        'message': 'Hello FastAPI to Python'
    }

@app.get('/users', tags=['users'])
def get_users():
    with engime.connect() as link:
        result = link.execute(users.select()).fetchall()
        return result

@app.get('/users/{id}', tags=['users'])
def get_user_by_id():
    with engime.connect() as link:
        result = link.execute(users.select().where(users.c.id == id)).first()
        return result