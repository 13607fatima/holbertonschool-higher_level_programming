#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the current square area.

        Returns:
            The current square area (int).
        """
        return self.__size ** 2
