class Road:
    def __init__(self, length):  
        self.length = length


class RacingRoad(Road):
    def __init__(self, length, speed_limit):
        super().__init__(length)
        self.speed_limit = speed_limit  

    def race(self, *cars):
        results = {}
        for car in cars:
            time = car.race(self.length, self.speed_limit)
            results[car.brand] = time
            print(f"{car.brand} finishes in {time:.2f} seconds")

        # Determine the winner (fastest time)
        winner = min(results, key=results.get)
        print(f"\n🏆 Winner is {winner}!")
        return winner

# Example usage
