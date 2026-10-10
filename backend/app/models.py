from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base

class BookingStatus(str, enum.Enum):
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

class Gender(str, enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone_number = Column(String(15), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    bookings = relationship("Booking", back_populates="user", cascade="all, delete-orphan")

class Station(Base):
    __tablename__ = "stations"

    station_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    station_code = Column(String(10), unique=True, nullable=False)
    station_name = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)

class Train(Base):
    __tablename__ = "trains"

    train_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    train_number = Column(String(10), unique=True, nullable=False)
    train_name = Column(String(100), nullable=False)
    total_seats = Column(Integer, nullable=False, default=100)

    schedules = relationship("Schedule", back_populates="train", cascade="all, delete-orphan")

class Schedule(Base):
    __tablename__ = "schedules"

    schedule_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    train_id = Column(Integer, ForeignKey("trains.train_id", ondelete="CASCADE"), nullable=False)
    source_station_id = Column(Integer, ForeignKey("stations.station_id"), nullable=False)
    destination_station_id = Column(Integer, ForeignKey("stations.station_id"), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    fare = Column(DECIMAL(10, 2), nullable=False)

    train = relationship("Train", back_populates="schedules")
    source_station = relationship("Station", foreign_keys=[source_station_id])
    destination_station = relationship("Station", foreign_keys=[destination_station_id])
    bookings = relationship("Booking", back_populates="schedule")

class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pnr_number = Column(String(10), unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    schedule_id = Column(Integer, ForeignKey("schedules.schedule_id"), nullable=False)
    booking_date = Column(TIMESTAMP, server_default=func.now())
    status = Column(Enum(BookingStatus), default=BookingStatus.CONFIRMED)
    total_amount = Column(DECIMAL(10, 2), nullable=False)

    user = relationship("User", back_populates="bookings")
    schedule = relationship("Schedule", back_populates="bookings")
    passengers = relationship("Passenger", back_populates="booking", cascade="all, delete-orphan")

class Passenger(Base):
    __tablename__ = "passengers"

    passenger_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id", ondelete="CASCADE"), nullable=False)
    passenger_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    seat_number = Column(String(10), nullable=False)

    booking = relationship("Booking", back_populates="passengers")