class Rational:
    def __init__(self, num=1, denum=1): # add check if arguments are int and add simplification of numbers
        self.__numerator = num
        self.__denominator = denum

    def __str__(self):
        return str(self.__numerator) + "/" + str(self.__denominator)

    def returnFraction(self):
        print(self.__str__())

    def printResult(self):
        print(eval(self.__str__()))

r = Rational(2, 3)
r.printResult()
