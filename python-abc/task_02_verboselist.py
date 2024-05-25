#!/usr/bin/python3
class VerboseList(list):
    """
    A subclass of list that prints messages when modifying the list."""
    def append(self, item):
        """Add a new item in the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list with an item and print a message."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Delete an item in the list and print a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Delete and return an item in the list and print a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
