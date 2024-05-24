from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Initialize the database
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    light_level = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


# Create the table
Base.metadata.create_all(bind=engine)

print("Database table created successfully.")
