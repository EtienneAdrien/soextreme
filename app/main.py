from typing import Union

import uvicorn
from fastapi import FastAPI

from app.utils.database.base import Base
from app.utils.database.connection import engine

from app.features.models import imports
imports()

metadata = Base.metadata
metadata.reflect(bind=engine)
metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def read_root():
    with engine.connect() as conn:
        res = conn.execute("SELECT 1;")
        print(res.fetchone())

    return {"Hello": "Adrien"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, debug=True, reload=True)
