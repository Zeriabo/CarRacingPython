class Car:
    def __init__(self, brand, max_speed, acceleration):
        self.brand = brand
        self.max_speed = max_speed        # km/h
        self.acceleration = acceleration  # m/s²

    def drive(self):
        print(f"{self.brand} is driving at max speed {self.max_speed} km/h")

    def race(self, distance, speed_limit):

        max_speed_m_s = self.max_speed * 1000 / 3600
        road_speed_m_s = speed_limit * 1000 / 3600


        effective_speed = min(max_speed_m_s, road_speed_m_s)


        d_accel = 0.5 * effective_speed**2 / self.acceleration

        if distance <= d_accel:

            time = (2 * distance / self.acceleration)**0.5
        else:

            t_accel = effective_speed / self.acceleration
            d_const = distance - d_accel
            t_const = d_const / effective_speed
            time = t_accel + t_const

        return time
class Ferrari(Car):
    pass

class McLaren(Car):
    pass