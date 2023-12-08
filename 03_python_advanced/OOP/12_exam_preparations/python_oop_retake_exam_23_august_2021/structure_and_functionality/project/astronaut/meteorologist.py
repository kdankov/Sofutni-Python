from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90
    DECREASE_UNITS = 15

    def __init__(self, name):
        super().__init__(name=name, oxygen=self.INITIAL_OXYGEN)

    @property
    def decrease_units(self):
        return self.DECREASE_UNITS
