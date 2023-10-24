#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square
"""


class Square():
    """Defines a square."""

    def __init__(self, size):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the length  of one edge.
        """
        self.__size = size
