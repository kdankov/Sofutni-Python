from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel: int, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
