import numbers


class Rectangle:
    def __paramSetter(self, number):
        maxVal = 20.0
        minVal = 0.0
        if isinstance(number, numbers.Number) and minVal < number < maxVal:
            return number
        else:
            raise TypeError("ERROR: can't change parameter to \"" + str(number) + "\"")

    def setWidth(self, width):
        temp = self.__paramSetter(width)
        self.__width = temp

    def setLength(self, length):
        temp = self.__paramSetter(length)
        self.__length = temp

    def __init__(self, width=None, length=None):
        if width is None and length is None:
            width, length = 1, 1
        self.setLength(length)
        self.setWidth(width)

    def getWidth(self):
        return self.__width

    def getLength(self):
        return self.__length

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return self.__length * 2 + self.__width * 2


try:
    r = Rectangle(1, 2)
    print("area: " + str(r.getArea()))
    print("perimeter: " + str(r.getPerimeter()))
except TypeError as e:
    print(e)
