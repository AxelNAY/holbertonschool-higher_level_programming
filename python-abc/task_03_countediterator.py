#!/usr/bin/python3

class CountedIterator:
    def __init__(self, item):
        """Initiate a counter for each item."""
        self.iterator = iter(item)
        self.counter = 0

    def get_count(self):
        """Return the counter"""
        return self.counter

    def __next__(self):
        """Update the counter and return the next item."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
