from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models import Ferrari, McLaren
from models import RacingRoad
from requestModels import RaceRequest
from requestModels import RoadRequest
app = FastAPI()

# Test root endpoint
@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

# Get info about a car
@app.get("/car/{brand}")
def get_car(brand: str):
    if brand.lower() == "ferrari":
        car = Ferrari("Ferrari", max_speed=340, acceleration=13)
    elif brand.lower() == "mclaren":
        car = McLaren("McLaren", max_speed=360, acceleration=11)
    else:
        return {"error": "Unknown car brand"}
    
    return {
        "brand": car.brand,
        "max_speed": car.max_speed,
        "acceleration": car.acceleration
    }

@app.post("/race")
def race(request: RaceRequest):
    # Create car objects dynamically based on request
    car_objects = []
    for car_data in request.cars:
        if car_data.brand.lower() == "ferrari":
            car_objects.append(Ferrari(car_data.brand, car_data.max_speed, car_data.acceleration))
        elif car_data.brand.lower() == "mclaren":
            car_objects.append(McLaren(car_data.brand, car_data.max_speed, car_data.acceleration))
        else:
            # Generic Car if brand unknown
            from cars import Car
            car_objects.append(Car(car_data.brand, car_data.max_speed, car_data.acceleration))

    # Create racing road from request
    road = RacingRoad(request.road.length, request.road.speed_limit)

    # Run the race
    results = {}
    for car in car_objects:
        time = car.race(road.length, road.speed_limit)
        results[car.brand] = round(time, 2)

    # Determine winner
    winner = min(results, key=results.get)

    return {
        "results": results,
        "winner": winner
    }
