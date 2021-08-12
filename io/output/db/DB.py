# Abstract DB class; extend this if you want to use a DB output

from abc import ABC, abstractmethod


class DB(ABC):
    def __init__(self):
        self.type = "generic"

    @abstractmethod
    def open_connection(self):
        print("Implement")

    @abstractmethod
    def close_connection(self):
        print("Implement")

    @abstractmethod
    def read(self):
        print("Implement")

    @abstractmethod
    def write_sync(self):
        print("Implement")

    @abstractmethod
    def write_async(self):
        print("Implement")