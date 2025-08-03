from fastapi import FastAPI, HTTPException
from db.models import Device, DeviceState
from utils.db_utils import SessionLocal, init_db
from uuid import UUID
from typing import List
from pydantic import BaseModel

init_db()

app = FastAPI(title="Device Control API")

class DeviceOut(BaseModel):
    id: UUID
    house_id: UUID
    name: str
    state: DeviceState

    class Config:
        orm_mode = True

@app.get("/devices/{house_id}", response_model=List[DeviceOut])
def get_devices_for_house(house_id: UUID):
    db = SessionLocal()
    devices = db.query(Device).filter(Device.house_id == house_id).all()
    db.close()
    return devices

@app.get("/device/{device_id}/status", response_model=DeviceOut)
def get_device_status(device_id: UUID):
    db = SessionLocal()
    device = db.query(Device).get(device_id)
    db.close()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@app.post("/device/{device_id}/on")
def turn_on_device(device_id: UUID):
    db = SessionLocal()
    device = db.query(Device).get(device_id)
    if not device:
        db.close()
        raise HTTPException(status_code=404, detail="Device not found")
    device.state = DeviceState.ON
    db.commit()
    db.close()
    return {"message": "Device turned ON"}

@app.post("/device/{device_id}/off")
def turn_off_device(device_id: UUID):
    db = SessionLocal()
    device = db.query(Device).get(device_id)
    if not device:
        db.close()
        raise HTTPException(status_code=404, detail="Device not found")
    device.state = DeviceState.OFF
    db.commit()
    db.close()
    return {"message": "Device turned OFF"}
