import numbers


class Rectangle:
    """ Class for working with a rectangle. """

    def __init__(self, width=1, length=1):
        """ Checks arguments against values and initializes class variables. """
        self.length = length
        self.width = width

    def __paramSetter(self, number):
        """ Interface for others setters. """
        maxVal = 20.0
        minVal = 0.0
        if not isinstance(number, numbers.Number):
            raise TypeError("argument is not a number")
        if not minVal < number < maxVal:
            raise ValueError("wrong value")
        return number

    @property
    def width(self):
        """ Returns width. """
        return self.__width

    @property
    def length(self):
        """ Returns length. """
        return self.__length

    @width.setter
    def width(self, width):
        """ Sets the width. """
        temp = self.__paramSetter(width)
        self.__width = temp

    @length.setter
    def length(self, length):
        """ Sets the length. """
        temp = self.__paramSetter(length)
        self.__length = temp

    def getArea(self):
        """ Counts and returns area. """
        return self.__length * self.__width

    def getPerimeter(self):
        """ Counts and returns perimeter. """
        return self.__length * 2 + self.__width * 2


try:
    rect = Rectangle(1, 2)
    print("area: " + str(rect.getArea()))
    print("perimeter: " + str(rect.getPerimeter()))
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
