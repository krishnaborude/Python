from fastapi.fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
 
 
app = FastAPI()
 
class User(BaseModel):
    Id: int
    name: str
    Age: int
    City: str
 
# In-memory data store
users = []
 
@app.get('/')
def home():
    return {"Message": "This is Home Page - Code is Successfully Running"}
 
@app.get('/user')
def show_user_data():
    return users
 
@app.post('/user')
def create_user(user: User):
    users.append(user)
    return {"Message": "User Created Successfully"}
 
@app.put('/user/{user_id}')
def update_user(user_id: int, update_user: User):
    for i, user in enumerate(users):
        if user.Id == user_id:
            users[i] = update_user
            return {"Message": "This User Successfully Updated"}
    return {"Message": "This User Not Updated Successfully"}
 
@app.delete('/user/{user_id}')
def delete_id(user_id: int):
    for i, user in enumerate(users):
        if user.Id == user_id:
            users.pop(i)
            return {"Message": "This User Deleted Successfully"}
    return {"Message": "Failed - Sorry Try Again Later"}
 
 
if __name__ == "__main__":
    uvicorn.run("Wan:app", host="127.0.0.1", port=8000)
 