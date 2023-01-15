from fastapi import FastAPI

import sel_add_method
import valid

app = FastAPI()


@app.get("/users/{user_id}")
async def users(id: int):
    user = sel_add_method.get_id(id)
    return {'id': user.id, 'login': user.login, 'email': user.email, 'phone': user.phone}


@app.post("/check")
async def check(user: valid.User):
    new_user = sel_add_method.add_user(user)
    return {'id': new_user.id}
