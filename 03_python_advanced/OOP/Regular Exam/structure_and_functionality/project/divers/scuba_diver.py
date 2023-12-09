from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name=name, oxygen_level=ScubaDiver.INITIAL_OXYGEN_LEVEL)

    @property
    def initial_oxygen_level(self):
        return ScubaDiver.INITIAL_OXYGEN_LEVEL

    @property
    def diver_type(self):
        return "ScubaDiver"

    @property
    def oxygen_reduce_percentage(self):
        return 0.3
