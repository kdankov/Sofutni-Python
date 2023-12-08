from typing import List


class Player:
    players_list: List[str] = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name not valid!")

        if value in self.players_list:
            raise ValueError(f"Name {value} is already used!")

        self.players_list.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"