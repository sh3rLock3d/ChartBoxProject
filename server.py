from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy import text

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:myPassword@localhost:5432/chartbox' 
engine = create_engine(SQLALCHEMY_DATABASE_URL,)
conn = engine.connect()


# todo add pydantic
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_user/{user_id}")
async def get_user(user_id):
    # todo validation of q, prevent sql injection
    q = f"SELECT * FROM users WHERE index={user_id}"
    output = conn.execute(text(q))
    results = output.fetchall()
    results = [i._mapping for i in list(results)]
    results = results[0] if results else None
    return {"message": results}


@app.get("/filter_user")
async def get_user(q = None,):
    # todo validation of q, prevent sql injection
    q = "SELECT * FROM users"
    output = conn.execute(text(q))
    results = output.fetchall()
    results = [i._mapping for i in list(results)]
    return {"message": results}

@app.get("/get_all_user")
async def get_user():
    q = "SELECT * FROM users"
    output = conn.execute(text(q))
    results = output.fetchall()
    results = [i._mapping for i in list(results)]
    return {"message": results[:10]}

