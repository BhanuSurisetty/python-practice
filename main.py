# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# user_db = {}

# # User schema
# class User(BaseModel):
#     username: str
#     full_name: str
#     email: str


# #Add user
# @app.post("/add_users")
# def add_user(user:User):
#     if user.username in user_db:
#         raise HTTPException(status_code=400, detail="Username already exists")
#     else:
#         user_db[user.username] = user
#         return {"message ": f"User {user.username} added successfully"}

# # get user
# @app.get("/get_user/{username}")
# def get_user(username:str):
#     if username not in user_db:
#         raise HTTPException(status_code = 404, detail ="User not found")
#     else:
#         return user_db[username]
    
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated DB
users_db = {}

# User schema
class User(BaseModel):
    username: str
    full_name: str
    email: str

# Route 1: Add a user
@app.post("/add_user")
def add_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = user
    return {"message": f"User {user.username} added successfully!"}

# Route 2: Get a user
@app.get("/get_user/{username}")
def get_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[username]
