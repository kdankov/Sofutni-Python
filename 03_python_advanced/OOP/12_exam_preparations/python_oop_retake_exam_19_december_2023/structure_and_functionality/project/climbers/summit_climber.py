from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150

    def __init__(self, name):
        super().__init__(name=name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        reduction = 0

        if peak.difficulty_level == "Advanced":
            reduction = 30 * 1.3
        elif peak.difficulty_level == "Extreme":
            reduction = 30 * 2.5

        self.strength -= reduction
        self.conquered_peaks.append(peak.name)