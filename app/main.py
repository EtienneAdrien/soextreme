from typing import Union

import uvicorn
from fastapi import FastAPI

from app.features.activity.routes import activity_router
from app.utils.database.base import Base
from app.utils.database.connection import engine

metadata = Base.metadata
metadata.reflect(bind=engine)
metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(activity_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, debug=True, reload=True)
