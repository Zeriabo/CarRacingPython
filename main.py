# main.py
from cars import Ferrari, McLaren  # Import classes from cars.py
from roads import RacingRoad        # Import class from roads.py

# Create cars
ferrari = Ferrari("Ferrari", max_speed=340, acceleration=13)
mclaren = McLaren("McLaren", max_speed=360, acceleration=11)

# Create racing road
road = RacingRoad(length=20000, speed_limit=360)
road.race(ferrari, mclaren)

