#!/usr/bin/python3

class Fish:
    """Class for the fish"""
    def swim(self):
        """Print that the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish live."""
        print("The fish lives in water")

class Bird:
    """Class for the bird"""
    def fly(self):
        """Print that the bird sky."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird live."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class for the flying fish"""
    def swim(self):
        """Print that the flying fish swim."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print that the flying fish plane."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print where the flying fish live."""
        print("The flying fish lives both in water and the sky!")
