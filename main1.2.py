from math import gcd


class Rational:
    """ Class for working with a rational fractions. """

    def __init__(self, num, denom):
        """ Initializes variables. """
        self.numerator = num
        self.denominator = denom
        self.__simplification()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, num):
        """ Sets numerator. """
        if not isinstance(num, int):
            raise TypeError("argument is not int")
        self.__numerator = num

    @denominator.setter
    def denominator(self, denom):
        """ Sets denominator. """
        if not isinstance(denom, int):
            raise TypeError("argument is not int")
        if denom == 0:
            raise ValueError("denominator = 0")
        self.__denominator = denom

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
    rational = Rational(5, 15)
    print(rational.returnFraction())
    print(rational.returnResult())
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
