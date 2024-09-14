from typing import Optional

from pydantic import BaseModel


class StationInformation(BaseModel):
    station_id: str
    name: str
    lat: float
    lon: float
    capacity: Optional[int] = 0


class StationStatus(BaseModel):
    station_id: str
    num_bikes_available: Optional[int] = 0
    num_docks_available: Optional[int] = 0
    num_ebikes_available: Optional[int] = 0
    num_bikes_disabled: Optional[int] = 0
    num_docks_disabled: Optional[int] = 0
    num_bikes_reserved: Optional[int] = 0
    num_docks_reserved: Optional[int] = 0
    is_installed: int = 0
    is_renting: int = 0
    is_returning: int = 0
