from abc import ABC


class Dao(ABC):
    def __init__(self, session):
        self.__session = session

    def get(self):
        pass

    def get_all(self):
        pass

    def create(self):
        pass

    @property
    def session(self):
        return self.__session