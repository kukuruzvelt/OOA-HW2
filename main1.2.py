from math import gcd


class Rational:
    """ Class for working with a rational fractions. """

    def __init__(self, num, denom):
        """ Checks arguments against values and initializes class variables. """
        if isinstance(num, int) and isinstance(denom, int):
            if denom == 0:
                raise ValueError("wrong value")
            else:
                self.__numerator = num
                self.__denominator = denom
                self.__simplification()
        else:
            raise TypeError("wrong arguments")

    def __simplification(self):
        """ Simplifies numbers by dividing them by the greatest common factor. """
        temp = gcd(self.__numerator, self.__denominator)
        self.__numerator //= temp
        self.__denominator //= temp

    def returnFraction(self):
        """ Counts and returns rational numbers in the form a/b. """
        return str(self.__numerator) + "/" + str(self.__denominator)

    def returnResult(self):
        """ Counts and returns rational numbers in floating-point format. """
        return eval(self.returnFraction())


try:
    r = Rational(5, 15)
    print(r.returnFraction())
    print(r.returnResult())
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
