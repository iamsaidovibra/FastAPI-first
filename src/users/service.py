from sqlmodel.ext.asyncio import AsyncSession
from .schemas import UserCreateModel, UserUpdateModel
from sqlmodel import select, desc
from .models import User

class UserService:
    async def get_all_users(self, session: AsyncSession):
        statement = select(User).order_by(desc(User.created_at))

        result = await session.exec(statement)

        return result.all()

    async def get_user(self, user_uid: str, session: AsyncSession):
        statement = select(User).where(User.uid == user_uid)

        result = await session.exec(statement)

        user = result.first()

        return user if user is not None else None

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(
            **user_data_dict
        )

        session.add(new_user)
        await session.commit()

    async def update_user(self, user_uid: str, update_data: UserUpdateModel, session: AsyncSession):
        user_to_update = sefl.get_user(user_uid, session)

        if user_to_update is not None: 
            update_data_dict = update_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(user_to_update, k, v)

            await session.commit()

            return user_to_update
        
        else:
            return None

    async def delete_user(self, user_uid: str, session: AsyncSession):
        user_to_delete = self.get_user(user_uid, session)

        if user_to_delete is not None:
            await session.delete(user_to_delete)

            await session.commit()
        
        else: 
            return None





