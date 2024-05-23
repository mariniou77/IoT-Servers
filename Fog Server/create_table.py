from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the DATABASE_URL; it should be in the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define a base class using the declarative_base function
Base = declarative_base()


# Define the SensorData model class
class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    light_level = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


# Create the sensor_data table
Base.metadata.create_all(bind=engine)

print("Table created successfully!")
