from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name=name, oxygen_level=FreeDiver.INITIAL_OXYGEN_LEVEL)

    @property
    def initial_oxygen_level(self):
        return FreeDiver.INITIAL_OXYGEN_LEVEL

    @property
    def diver_type(self):
        return "FreeDiver"

    @property
    def oxygen_reduce_percentage(self):
        return 0.6

