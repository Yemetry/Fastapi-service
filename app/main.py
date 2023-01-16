import uvicorn
from fastapi import FastAPI

import sel_add_method, valid

app = FastAPI()


# The method receives a number (user id) as input, then we look for a string in the database whose id is the same and get a string for this id
@app.get("/users/{user_id}")
async def users(id: int):
    user = sel_add_method.get_id(id)
    if user is None:
        return 0

    return {'id': user.id, 'login': user.login, 'email': user.email, 'phone': user.phone}


# This method creates a new user using the data after the checks
@app.post("/check")
async def check(user: valid.User):
    new_user = sel_add_method.add_user(user)
    return {'id': new_user.id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
