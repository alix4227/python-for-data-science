from S1E7 import Baratheon, Lannister
class King(Baratheon, Lannister):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, family_name='Baratheon', eyes='brown', hairs='dark'):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
    def get_eyes(self):
        return(self.eyes)
    def get_hairs(self):
        return(self.hairs)
    def set_eyes(self, eyes):
        self.eyes = eyes
    def set_hairs(self, hairs):
        self.hairs = hairs