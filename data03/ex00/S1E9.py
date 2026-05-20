from abc import ABC, abstractmethod
class Character(ABC):
    """
    Your docstring for Class
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.firstname = first_name
        self.is_alive = is_alive
    def die(self):
        self.is_alive = False

class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
