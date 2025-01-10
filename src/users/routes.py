from typing import List
from fastapi import FastAPI, status, APIRouter
from fastapi.exceptions import HTTPException
from src.users.user_data import users
from src.users.schemas import User, UserUpdate

user_router = APIRouter()

@user_router.get("/", response_model=List[User])
async def get_all_users():
    return users

@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_user(user_data: User) -> dict:
    new_user = user_data.model_dump()
    users.append(new_user)

    return new_user

@user_router.patch("/{user_id}")
async def update_user(user_id: int, user_update_data: UserUpdate) -> dict:
    for user in users:
        if user['id'] == user_id:
            user['email'] = user_update_data.email
            user['phone_num'] = user_update_data.phone_num

            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="User not found") 

@user_router.get("/{user_id}")
async def get_a_user_by_id(user_id: int) -> dict:
    for user in users:
        if user['id'] == user_id:
            return user
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found")

@user_router.delete("/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return {"message": f"User {user_id} was removed"}

    raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found")

