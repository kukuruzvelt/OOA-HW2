from math import gcd


class Rational:
    def __init__(self, num, denom):
        if isinstance(num, int) and isinstance(denom, int):
            self.__numerator = num
            self.__denominator = denom
            self.__simplification()
        else:
            raise TypeError("wrong arguments")

    def __simplification(self):
        temp = gcd(self.__numerator, self.__denominator)
        self.__numerator //= temp
        self.__denominator //= temp

    def returnFraction(self):
        return str(self.__numerator) + "/" + str(self.__denominator)

    def returnResult(self):
        return eval(self.returnFraction())


try:
    r = Rational(5, 15)
    print(r.returnFraction())
    print(r.returnResult())
except TypeError as e:
    print("ERROR")
