#!/usr/bin/python3
"""
This is the base module
It contains the "base" to be used throughout the project
"""


class Base():
    """
    The base of all other classes in the project.
    Used to manage the id attribute to avoid code duplication.
    Attributes:
        __nb_objects (int): Number of Base objects
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """
        Initialized the default attributes
        Args:
            id (int): Identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
