from fastapi import FastAPI

from app.routers.events import router as events_router


app = FastAPI(title="Campus Pass API")


app.include_router(events_router)
