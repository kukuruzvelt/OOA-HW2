import numbers


class Rectangle:  # make width and length private
    def __init__(self):
        self.__width, self.__length = 1, 1

    def __paramSetter(self, number):
        maxVal = 20.0
        minVal = 0.0
        if isinstance(number, numbers.Number) and minVal < number < maxVal:
            return number
        else:
            raise Exception("ERROR: can't change parameter to \"" + str(number) + "\"")

    def setWidth(self, width):
        try:
            temp = self.__paramSetter(width)
            self.__width = temp
        except Exception as e:
            print(e)

    def setLength(self, length):
        try:
            temp = self.__paramSetter(length)
            self.__length = temp
        except Exception as e:
            print(e)

    def getWidth(self):
        return self.__width

    def getLength(self):
        return self.__length

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return self.__length * 2 + self.__width * 2


r = Rectangle()
r.setLength(10)
r.setLength("a")
r.setWidth(19)
r.setWidth(-1)
print("area: " + str(r.getArea()))
print("perimeter: " + str(r.getPerimeter()))

