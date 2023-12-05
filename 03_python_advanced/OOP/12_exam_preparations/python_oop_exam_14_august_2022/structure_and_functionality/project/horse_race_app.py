from typing import List

from project.jockey import Jockey
from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self._get_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            new_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self._get_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self._get_race_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_race_type = HorseRace(race_type)
        self.horse_races.append(new_race_type)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._get_jockey_by_name(jockey_name)
        horse = self._get_last_added_horse_of_given_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._get_race_by_type(race_type)
        jockey = self._get_jockey_by_name(jockey_name)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for race_jockey in race.jockeys:
            if jockey.name == race_jockey.name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._get_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        current_max_speed = 0

        for jockey in race.jockeys:
            if jockey.horse.speed > current_max_speed:
                winner = jockey
                current_max_speed = jockey.horse.speed

        return (f"The winner of the {race_type} race, with a speed of {current_max_speed}km/h is {winner.name}!"
                f" Winner's horse: {winner.horse.name}.")

    def _get_horse_by_name(self, horse_name: str):
        collection = [x for x in self.horses if x.name == horse_name]
        return collection[0] if collection else None

    def _get_jockey_by_name(self, jockey_name: str):
        collection = [x for x in self.jockeys if x.name == jockey_name]
        return collection[0] if collection else None

    def _get_race_by_type(self, race_type: str):
        collection = [x for x in self.horse_races if x.race_type == race_type]
        return collection[0] if collection else None

    def _get_last_added_horse_of_given_type(self, horse_type):
        collection = [x for x in self.horses[::-1] if x.__class__.__name__ == horse_type and not x.is_taken]
        return collection[0] if collection else None