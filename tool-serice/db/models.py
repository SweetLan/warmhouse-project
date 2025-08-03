from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import enum
import uuid

Base = declarative_base()

class DeviceState(str, enum.Enum):
    ON = "ON"
    OFF = "OFF"
    UNKNOWN = "UNKNOWN"

class Device(Base):
    __tablename__ = 'devices'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    house_id = Column(UUID(as_uuid=True), nullable=False)
    type_id = Column(UUID(as_uuid=True), nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    state = Column(Enum(DeviceState), default=DeviceState.UNKNOWN)
    name = Column(String)
