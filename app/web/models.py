"""models: models pertaining to transit routes"""
from typing import Optional

from pydantic import BaseModel


class RouteModel(BaseModel):
    """Model for transit routes"""

    id: str
    long_name: str
    short_name: str
    description: str
    direction: tuple[str, str]
    destinations: tuple[str, str]


class StopModel(BaseModel):
    """Model for transit stops"""

    id: str
    name: str
    municipality: str
    description: Optional[str]
    address: Optional[str]
    lat_long: tuple[Optional[float], Optional[float]]
