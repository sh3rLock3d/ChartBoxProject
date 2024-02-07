from fastapi import FastAPI





# todo add pydantic
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_user/{user_id}")
async def get_user(user_id):
    return {"message": user_id}