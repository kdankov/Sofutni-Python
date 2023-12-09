from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH = 90

    def __init__(self, name: str, points: float):
        super().__init__(name=name, points=points, time_to_catch=PredatoryFish.TIME_TO_CATCH)

    @property
    def fish_type(self):
        return "PredatoryFish"
