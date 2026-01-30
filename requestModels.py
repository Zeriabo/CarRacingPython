from pydantic import BaseModel
from typing import List

class CarRequest(BaseModel):
    brand: str
    max_speed: float       
    acceleration: float    
class RaceRequest(BaseModel):
    cars: List[CarRequest]
    road: RoadRequest
class RoadRequest(BaseModel):
    length: float          
    speed_limit: float     
