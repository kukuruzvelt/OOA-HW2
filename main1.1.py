import numbers


class Rectangle:
    """ Class for working with a rectangle. """

    def __paramSetter(self, number):
        """ Interface for others setters. """
        maxVal = 20.0
        minVal = 0.0
        if isinstance(number, numbers.Number):
            if not minVal < number < maxVal:
                raise ValueError("wrong value")
            else:
                return number
        else:
            raise TypeError("wrong arguments")

    def setWidth(self, width):
        """ Sets the width. """
        temp = self.__paramSetter(width)
        self.__width = temp

    def setLength(self, length):
        """ Sets the length. """
        temp = self.__paramSetter(length)
        self.__length = temp

    def __init__(self, width=None, length=None):
        """ Checks arguments against values and initializes class variables. """
        if width is None and length is None:
            width, length = 1, 1
        self.setLength(length)
        self.setWidth(width)

    def getWidth(self):
        """ Returns width. """
        return self.__width

    def getLength(self):
        """ Returns length. """
        return self.__length

    def getArea(self):
        """ Counts and returns area. """
        return self.__length * self.__width

    def getPerimeter(self):
        """ Counts and returns perimeter. """
        return self.__length * 2 + self.__width * 2


try:
    r = Rectangle(1, 2)
    print("area: " + str(r.getArea()))
    print("perimeter: " + str(r.getPerimeter()))
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
