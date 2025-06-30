from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, crud
from .database import engine, get_db
from .redis_cache import get_cache, set_cache
import time

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.Item])
async def read_items(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    cache_key = f"items_{skip}_{limit}"
    cached = await get_cache(cache_key)
    if cached:
        return cached
    time.sleep(5)
    items = await crud.get_items(db, skip=skip, limit=limit)
    await set_cache(cache_key, [schemas.Item.from_orm(i).dict() for i in items])
    return items

@app.get("/")
def read_root():
    return {"message": "FastAPI + PostgreSQL + Redis is running!"}
