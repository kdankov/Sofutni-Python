from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if not value.strip():
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.restriction_age:
            raise ValueError(f'{self.__class__.__name__} movies must be restricted for audience under '
                             f'{self.restriction_age} years!')

        self.__age_restriction = value

    @property
    @abstractmethod
    def restriction_age(self):
        pass

    def details(self):
        return (f'{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, '
                f'Age restriction:{self.age_restriction}, Likes:{self.likes}, '
                f'Owned by:{self.owner.username}')
