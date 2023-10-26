#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the length of one edge.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character on stdout."""
        if self.__size > 0:
            for x in range(self.__size):
                print('#' * self.__size)
        else:
            print()
