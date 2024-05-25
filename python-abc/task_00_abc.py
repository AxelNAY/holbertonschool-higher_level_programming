#!/usr/bin/python3


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Class"""
    @abstractmethod
    def sound(self):
        """Sound made by an animal"""
        pass

class Dog(Animal):
    """Class dog"""
    def sound(self):
        """Return the sound made by a dog"""
        return "Bark"


class Cat(Animal):
    """Class cat"""
    def sound(self):
        """Return the sound made by a cat"""
        return "Meow"
