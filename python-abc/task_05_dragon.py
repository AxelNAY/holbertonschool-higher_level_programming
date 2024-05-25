#!/usr/bin/python3

class SwimMixin:
    """Class for the action swim"""
    def swim(self):
        """Print that the creature swim"""
        print("The creature swims!")

class FlyMixin:
    """Class for the action fly"""
    def fly(self):
        """Print that the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class for the dragon"""
    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
