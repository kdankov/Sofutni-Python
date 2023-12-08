from typing import List

from project.player import Player
from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink


class Controller:
    VALID_SUSTENANCE_TYPES = {
        "Food": Food,
        "Drink": Drink
    }

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        added_players = []

        for player in args:
            if not self._get_player_by_name(player.name):
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args: Supply):
        [self.supplies.append(supply) for supply in args]

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.VALID_SUSTENANCE_TYPES:
            return

        player = self._get_player_by_name(player_name)

        if player is None:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        last_supply_index = self._get_last_index_of_supply_by_type(sustenance_type)

        if last_supply_index is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        supply = self.supplies.pop(last_supply_index)

        player.stamina = min(100, player.stamina + supply.energy)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self._get_player_by_name(first_player_name)
        second_player = self._get_player_by_name(second_player_name)

        result = self._check_if_the_players_cannot_duel(first_player, second_player)

        if result:
            return result

        return self._attack(first_player, second_player)

    def next_day(self):
        for player in self.players:
            reduce_amount = player.age * 2
            player.stamina = max(0, player.stamina - reduce_amount)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        [result.append(player.__str__()) for player in self.players]
        [result.append(supply.details()) for supply in self.supplies]

        return "\n".join(result)

    @staticmethod
    def _check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    @staticmethod
    def _attack(first_player: Player, second_player: Player):
        winner = None
        attacker, defender = [second_player, first_player] if first_player.stamina > second_player.stamina \
            else [first_player, second_player]

        attacker_damage = attacker.stamina / 2
        defender.stamina = max(0, defender.stamina - attacker_damage)

        if not defender.stamina:
            winner = attacker

        if not winner:
            defender_damage = defender.stamina / 2
            attacker.stamina = max(0, attacker.stamina - defender_damage)

        if not attacker.stamina:
            winner = defender

        if winner is None:
            winner = first_player if first_player.stamina > second_player.stamina \
                else second_player

        return f"Winner: {winner.name}"

    def _get_player_by_name(self, name):
        collection = [x for x in self.players if x.name == name]
        return collection[0] if collection else None

    def _get_last_index_of_supply_by_type(self, sustenance_type):
        for supply_index in range(len(self.supplies) - 1, - 1, -1):
            if self.supplies[supply_index].__class__.__name__ == sustenance_type:
                return supply_index
