from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from typing import List


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.__get_diver_by_name(diver_name):
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.__get_fish_by_name(fish_name):
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.__get_diver_by_name(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        fish = self.__get_fish_by_name(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if not is_lucky:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_divers_count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.renew_oxy()
                diver.update_health_status()
                recovered_divers_count += 1

        return f"Divers recovered: {recovered_divers_count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.__get_diver_by_name(diver_name)

        if not diver:
            return

        result = [f"**{diver_name} Catch Report**"]
        [result.append(fish.fish_details()) for fish in diver.catch]

        return "\n".join(result)

    def competition_statistics(self):
        sorted_divers = sorted([diver for diver in self.divers if not diver.has_health_issue],
                               key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        result = [f"**Nautical Catch Challenge Statistics**"]
        [result.append(diver.__str__()) for diver in sorted_divers]

        return "\n".join(result)

    def __get_diver_by_name(self, diver_name):
        return next(filter(lambda d: d.name == diver_name, self.divers), None)

    def __get_fish_by_name(self, fish_name):
        return next(filter(lambda f: f.name == fish_name, self.fish_list), None)
