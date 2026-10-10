from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional
from enum import Enum

class GenderEnum(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class BookingStatusEnum(str, Enum):
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

# Station Schemas
class StationBase(BaseModel):
    station_code: str
    station_name: str
    city: str

class StationResponse(StationBase):
    station_id: int

    class Config:
        from_attributes = True

# Train Schemas
class TrainBase(BaseModel):
    train_number: str
    train_name: str
    total_seats: int

class TrainResponse(TrainBase):
    train_id: int

    class Config:
        from_attributes = True

# Schedule Schemas
class ScheduleResponse(BaseModel):
    schedule_id: int
    train: TrainResponse
    source_station: StationResponse
    destination_station: StationResponse
    departure_time: datetime
    arrival_time: datetime
    fare: float

    class Config:
        from_attributes = True

# User Schemas
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    password: str

class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    phone_number: str

    class Config:
        from_attributes = True