#!/usr/bin/python3
"""
This is the rectangle module
It contains implementation of Rectangle inheriting from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle object
    Attributes:
        __width (int): Length of the width
        __height(int): Length of the height
        __x (int): The horizontal padding of the rectangle
        __y (int): The vertical padding of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the default attributes of the rectangle
        Args:
        __width (int): Length of the width
        __height(int): Length of the height
        __x (int): The horizontal padding of the rectangle
        __y (int): The vertical padding of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
