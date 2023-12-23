from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name):
        super().__init__(name=name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        reduction = 0

        if peak.difficulty_level == "Extreme":
            reduction = 20 * 2
        elif peak.difficulty_level == "Advanced":
            reduction = 20 * 1.5

        self.strength -= reduction
        self.conquered_peaks.append(peak.name)