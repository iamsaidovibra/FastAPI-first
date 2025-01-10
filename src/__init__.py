from fastapi import FastAPI
from src.users.routes import user_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("\n", f"---SERVER IS STARTING...---", "\n")
    await init_db()
    yield                                             
    print("\n", f"---SERVER HAS BEEN STOPPED---", "\n")


version = "v1"

app = FastAPI(
    title="Userly",
    description="A REST API for a user bla bla bla",
    versioon=version,
    lifespan=life_span,
)
     
app.include_router(user_router, prefix=f"/api/{version}/users", tags=['users'])
