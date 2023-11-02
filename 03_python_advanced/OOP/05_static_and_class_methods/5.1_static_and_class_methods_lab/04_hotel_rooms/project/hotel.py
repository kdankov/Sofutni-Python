from project.room import Room
from typing import List


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: str, people: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self) -> str:
        return (f'Hotel {self.name} has {self.guests} total guests'
                f'\nFree rooms: {", ".join([str(room.number) for room in self.rooms if not room.is_taken])}'
                f'\nTaken rooms: {", ".join([str(room.number) for room in self.rooms if room.is_taken])}')
