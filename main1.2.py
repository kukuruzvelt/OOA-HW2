class Rational:
    def __init__(self, num=1, denom=1):
        self.__numerator = num
        self.__denominator = denom
        self.__simplification()

    def __simplification(self):
        for i in range(2, 10):
            temp1 = self.__numerator / i
            temp2 = self.__denominator / i
            if temp1.is_integer() and temp2.is_integer():
                self.__numerator = int(temp1)
                self.__denominator = int(temp2)
                break

    def returnFraction(self):
        return str(self.__numerator) + "/" + str(self.__denominator)

    def printResult(self):
        return eval(self.returnFraction())

try:
    r = Rational(5, 15)
    print(r.returnFraction())
    print(r.printResult())
except TypeError as e:
    print("ERROR")
