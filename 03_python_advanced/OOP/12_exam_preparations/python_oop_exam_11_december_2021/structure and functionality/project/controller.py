from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race
from typing import List


class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPES:
            return

        if self.__get_car_by_model(model):
            raise Exception(f"Car {model} is already created!")

        new_car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__get_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__get_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        new_car = self.__get_last_added_car_of_given_type(car_type)
        if not new_car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            return self.__change_cars(driver, new_car)

        driver.car = new_car
        new_car.is_taken = True
        return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__get_driver_by_name(driver_name)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if self.__check_if_driver_is_in_race(driver, race):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        return self.race(race)

    def __get_car_by_model(self, model):
        collection = [x for x in self.cars if x.model == model]
        return collection[0] if collection else None

    def __get_driver_by_name(self, name):
        collection = [x for x in self.drivers if x.name == name]
        return collection[0] if collection else None

    def __get_race_by_name(self, name):
        collection = [x for x in self.races if x.name == name]
        return collection[0] if collection else None

    def __get_last_added_car_of_given_type(self, car_type):
        car = None
        for current_car in self.cars:
            if current_car.__class__.__name__ == car_type and not current_car.is_taken:
                car = current_car
        return car

    @staticmethod
    def race(race: Race):
        top_drivers = sorted(race.drivers, key=lambda d: -d.car.speed_limit)[:3]

        result = []
        for driver in top_drivers:
            result.append(f"Driver {driver.name} wins the {race.name} race with a speed of {driver.car.speed_limit}.")
            driver.number_of_wins += 1

        return "\n".join(result)

    @staticmethod
    def __check_if_driver_is_in_race(driver: Driver, race: Race):
        return [d for d in race.drivers if d.name == driver.name]

    @staticmethod
    def __change_cars(driver: Driver, new_car: Car):
        old_car = driver.car
        old_car.is_taken = False
        driver.car = new_car
        new_car.is_taken = True
        return f"Driver {driver.name} changed his car from {old_car.model} to {new_car.model}."