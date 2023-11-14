#!/usr/bin/python3
"""
The square module
Contains implementation of Square inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square object, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the default attributes of the Square
        Args:
           size (int): Length of one side.
           x (int): Horizontal (x) padding of the square.
           y (int): Vertical (y) padding of the square.
           id (int): Identifier
        """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """
        Return attributes in [Square] (<id>) <x>/<y> - <size> format
        """
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"
