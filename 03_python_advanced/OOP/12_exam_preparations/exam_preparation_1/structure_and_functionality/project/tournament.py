from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {'KneePad': KneePad,
                             'ElbowPad': ElbowPad}

    VALID_TEAM_TYPES = {'OutdoorTeam': OutdoorTeam,
                        'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')

        self.__name = value

    def add_equipment(self, equipment_type: str) -> str or Exception:
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception('Invalid equipment type!')

        equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment)
        return f'{equipment_type} was successfully added.'

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str or Exception:
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception('Invalid team type!')

        if len(self.teams) >= self.capacity:
            return f'Not enough tournament capacity.'

        team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f'{team_type} was successfully added.'

    def sell_equipment(self, equipment_type: str, team_name: str) -> str or Exception:
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment)))

        if team.budget <= equipment.price:
            raise Exception('Budget is not enough!')

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f'Successfully sold {equipment_type} to {team_name}.'

    def remove_team(self, team_name: str) -> str or Exception:
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception('No such team!')

        if team.wins > 0:
            raise Exception(f'The team has {team.wins} wins! Removal is impossible!')

        self.teams.remove(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type: str) -> str:
        number_of_changed_equipment = 0

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                number_of_changed_equipment += 1

        return f'Successfully changed {number_of_changed_equipment}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception('Game cannot start! Team types mismatch!')

        team1_points = self.get_team_points(team1)
        team2_points = self.get_team_points(team2)

        winner = team1 if team1_points > team2_points else team2 if team2_points > team1_points else None

        if winner is None:
            return 'No winner in this game.'

        winner.win()
        return f'The winner is {winner.name}.'

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda t: -t.wins)

        result = [f'Tournament: {self.name}',
                  f'Number of Teams: {len(self.teams)}',
                  'Teams:']
        [result.append(t.get_statistics()) for t in teams]

        return '\n'.join(result)

    @staticmethod
    def get_team_points(team: BaseTeam):
        return team.advantage + sum(e.protection for e in team.equipment)

