from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name=name, oxygen=self.INITIAL_OXYGEN)

    @property
    def decrease_units(self):
        return self.DECREASE_UNITS
