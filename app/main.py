from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db
from .redis_cache import get_cache, set_cache
import time
from contextlib import asynccontextmanager
from .mcp_client import send_to_mcp

@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cache_key = f"items_{skip}_{limit}"
    cached = get_cache(cache_key)
    if cached:
        return cached
    time.sleep(2)
    items = crud.get_items(db, skip=skip, limit=limit)
    set_cache(cache_key, [schemas.Item.model_validate(i).model_dump() for i in items])
    return items

@app.get("/")
def read_root():
    return {"message": "FastAPI + PostgreSQL + Redis is running!"}


from .mcp_client import send_to_mcp

@app.post("/ask/")
async def ask_mcp(question: str):
    response = await send_to_mcp(question)
    return response
