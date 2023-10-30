from project.album import Album
from project.song import Song
from typing import List


class Band:
    def __init__(self, name):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str) -> str:
        try:
            album = next(filter(lambda x: x.name == album_name, self.albums))
        except StopIteration:
            return f'Album {album_name} is not found.'

        if album.published:
            return f'Album has been published. It cannot be removed.'

        self.albums.remove(album)
        return f'Album {album_name} has been removed.'

    def details(self) -> str:
        result = [f'Band {self.name}']
        [result.append(f'{album.details()}') for album in self.albums]

        return '\n'.join(result)
