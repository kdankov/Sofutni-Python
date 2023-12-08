from abc import ABC, abstractmethod


class Astronaut(ABC):
    DECREASE_UNITS = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @property
    @abstractmethod
    def decrease_units(self):
        pass

    def breathe(self):
        self.oxygen -= self.DECREASE_UNITS

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        return f"""Name: {self.name}
Oxygen: {self.oxygen}
Backpack items: {', '.join([i for i in self.backpack]) if self.backpack else "none"}"""