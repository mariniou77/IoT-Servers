from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from databases import Database
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load environment variables from a .env file
load_dotenv()

app = FastAPI()

# Correctly set the DATABASE_URL with the actual credentials
DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    light_level = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class SensorDataCreate(BaseModel):
    light_level: float
    latitude: float
    longitude: float


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)


@app.post("/data/")
async def receive_data(data: SensorDataCreate):
    query = SensorData.__table__.insert().values(
        light_level=data.light_level,
        latitude=data.latitude,
        longitude=data.longitude
    )
    await database.execute(query)
    return {"message": "Data received successfully", "data": data}


@app.get("/data/")
async def get_all_data():
    query = SensorData.__table__.select()
    return await database.fetch_all(query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
