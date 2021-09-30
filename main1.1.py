import numbers


class Rectangle: #make width and length private
    def __init__(self):
        self.width, self.length = 1, 1

    def __paramSetter(self, number):
        maxVal = 20.0
        minVal = 0.0
        if isinstance(number, numbers.Number) and minVal < number < maxVal:
            return number
        else:
            print("ERROR: can't change parameter to \"" + str(number) + "\"")

    def setWidth(self, width):
        temp = self.__paramSetter(width)
        if temp:
            self.width = temp

    def setLength(self, length):
        temp = self.__paramSetter(length)
        if temp:
            self.length = temp

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return self.length * 2 + self.width * 2


r = Rectangle()
r.setLength(10)
r.setLength("a")
r.setWidth(19)
r.setWidth(-1)
print("area: " + str(r.getArea()))
print("perimeter: " + str(r.getPerimeter()))
r2 = Rectangle()
