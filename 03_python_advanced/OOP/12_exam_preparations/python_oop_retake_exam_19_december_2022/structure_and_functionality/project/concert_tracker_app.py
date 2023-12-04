from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert
from typing import List


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        'Guitarist': Guitarist,
        'Drummer': Drummer,
        'Singer': Singer
    }

    # drummer_skills = {
    #     'Rock': 'play the drums with drumsticks',
    #     'Metal': 'play the drums with drumsticks',
    #     'Jazz': 'play the drums with drum brushes'
    # }
    # singer_skills = {
    #     'Rock': 'sing high pitch notes',
    #     'Metal': 'sing low pitch notes',
    #     'Jazz': ['sing high pitch notes', 'sing low pitch notes']
    # }
    # guitarist_skills = {
    #     'Rock': 'play rock',
    #     'Metal': 'play metal',
    #     'Jazz': 'play jazz'
    # }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError('Invalid musician type!')

        if self._get_musician_by_name(name, self.musicians):
            raise Exception(f'{name} is already a musician!')

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)

        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if self._get_band_by_name(name):
            raise Exception(f'{name} band is already created!')

        new_band = Band(name)
        self.bands.append(new_band)
        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_concert_by_place(place)
        if concert:
            raise Exception(f'{place} is already registered for {concert.genre} concert!')

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f'{new_concert.genre} concert in {new_concert.place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_musician_by_name(musician_name, self.musicians)
        band = self._get_band_by_name(band_name)

        if not musician:
            raise Exception(f'{musician_name} isn\'t a musician!')

        if not band:
            raise Exception(f'{band_name} isn\'t a band!')

        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_band_by_name(band_name)
        if not band:
            raise Exception(f'{band_name} isn\'t a band!')

        musician = self._get_musician_by_name(musician_name, band.members)
        if not musician:
            raise Exception(f'{musician_name} isn\'t a member of {band_name}!')

        band.members.remove(musician)
        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):
        band = self._get_band_by_name(band_name)
        if not self._check_band_members_types(band):
            raise Exception(f'{band_name} can\'t start the concert because it doesn\'t have enough members!')

        concert = self._get_concert_by_place(concert_place)

        if not self._check_band_members_for_needed_skills(band, concert.genre):
            raise Exception(f'The {band_name} band is not ready to play at the concert!')

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'

    @staticmethod
    def _get_musician_by_name(name, collection):
        result = [m for m in collection if m.name == name]
        return result[0] if result else None

    def _get_band_by_name(self, band_name):
        collection = [b for b in self.bands if b.name == band_name]
        return collection[0] if collection else None

    def _get_concert_by_place(self, place):
        collection = [c for c in self.concerts if c.place == place]
        return collection[0] if collection else None

    def _check_band_members_types(self, band: Band):
        band_musicians_types = set([m.__class__.__name__ for m in band.members])
        return len(band_musicians_types) == len(self.VALID_MUSICIAN_TYPES)

    def _check_band_members_for_needed_skills(self, band: Band, concert_genre):
        required_skills = {
            'Rock': {
                'Drummer': ['play the drums with drumsticks'],
                'Guitarist': ['play rock'],
                'Singer': ['sing high pitch notes']
            },
            'Metal': {
                'Drummer': ['play the drums with drumsticks'],
                'Guitarist': ['play metal'],
                'Singer': ['sing low pitch notes']
            },
            'Jazz': {
                'Drummer': ['play the drums with drum brushes'],
                'Guitarist': ['play jazz'],
                'Singer': ['sing high pitch notes', 'sing low pitch notes']
            }
        }

        for musician_type, needed_skills in required_skills[concert_genre].items():
            collection = [m for m in band.members if
                          m.__class__.__name__ == musician_type and all([s in m.skills for s in needed_skills])]
            if not collection:
                return False
        return True