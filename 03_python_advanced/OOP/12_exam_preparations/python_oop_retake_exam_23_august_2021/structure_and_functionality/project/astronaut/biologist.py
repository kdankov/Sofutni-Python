from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN = 70
    DECREASE_UNITS = 5

    def __init__(self, name: str):
        super().__init__(name=name, oxygen=self.INITIAL_OXYGEN)

    @property
    def decrease_units(self):
        return self.DECREASE_UNITS
