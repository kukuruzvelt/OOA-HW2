import numbers
import re


class Product:
    """ Class for working with products. """

    def __init__(self, price, description, dimensions):
        """ Checks arguments against values and initializes class variables. """
        if (isinstance(price, numbers.Number) and isinstance(description, str)
                and isinstance(dimensions, numbers.Number)):
            if price < 0:
                raise ValueError("wrong value")
            self.__price = price
            self.__description = description
            self.__dimensions = dimensions
        else:
            raise TypeError("wrong arguments")

    def getPrice(self):
        """ Returns price. """
        return self.__price


class Customer:
    """ Class for working with customers. """

    def __init__(self, name, surname, mobile_phone):
        """ Checks arguments against values and initializes class variables. """
        if isinstance(name, str) and isinstance(surname, str) and isinstance(mobile_phone, str):
            if not name or not surname or not len(mobile_phone) == 10 or not re.match(r'[0][0-9]{9}', mobile_phone):
                raise ValueError("wrong value")
            else:
                self.__name = name
                self.__surname = surname
                self.__mobile_phone = mobile_phone
        else:
            raise TypeError("wrong arguments")

    def getName(self):
        """ Returns name. """
        return self.__name

    def getSurname(self):
        """ Returns surname. """
        return self.__surname

    def getMobilePhone(self):
        """ Returns phone number. """
        return self.__mobile_phone


class Order:
    """ Class for working with orders. """

    def __init__(self, customer, products):
        """ Checks arguments against values and initializes class variables. """
        if (isinstance(products, list) and all(isinstance(x, Product) for x in products)
                and isinstance(customer, Customer)):
            self.__customer = customer
            self.__products = products
        else:
            raise TypeError("wrong arguments")

    def getTotalPrice(self):
        """ Counts and returns total price. """
        total_prise = 0
        for i in range(len(self.__products)):
            total_prise += self.__products[i].getPrice()
        return total_prise

    def addProduct(self, product):
        """ Adds a product. """
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("wrong arguments")

    def delProduct(self, product):
        """ Removes the product. """
        if isinstance(product, Product):
            self.__products.remove(product)
        else:
            raise TypeError("wrong arguments")


try:
    p1 = Product(1, "first_product", 1)
    p2 = Product(2, "second_product", 2)
    p3 = Product(3, "third_product", 3)
    c = Customer("Sergey", "Kurnosenko", "0951713987")
    o = Order(c, [p1, p2])
    o.addProduct(p3)
    o.delProduct(p2)
    print("total price = ", o.getTotalPrice())
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
