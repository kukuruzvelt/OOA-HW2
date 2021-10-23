import numbers
import re


class Product:
    """ Class for working with products. """

    def __init__(self, price, description, dimensions):
        """ Initializes variables. """
        self.setPrice(price)
        self.setDescription(description)
        self.setDimensions(dimensions)

    def setPrice(self, price):
        """ Sets price. """
        if not isinstance(price, numbers.Number):
            raise TypeError("argument is not a number")
        if price < 0:
            raise ValueError("price < 0")
        self.__price = price

    def setDescription(self, description):
        """ Sets description. """
        if not isinstance(description, str):
            raise TypeError("argument is not a string")
        self.__description = description

    def setDimensions(self, dimensions):
        """ Sets dimensions. """
        if not isinstance(dimensions, numbers.Number):
            raise TypeError("argument is not a number")
        self.__dimensions = dimensions

    def getPrice(self):
        """ Returns price. """
        return self.__price


class Customer:
    """ Class for working with customers. """

    def __init__(self, name, surname, mobile_phone):
        """ Initializes variables. """
        self.setName(name)
        self.setSurname(surname)
        self.setMobilePhone(mobile_phone)

    def setName(self, name):
        """ Sets name. """
        if not isinstance(name, str):
            raise TypeError("argument is not a string")
        if not name:
            raise ValueError("wrong value")
        self.__name = name

    def setSurname(self, surname):
        """ Sets surname. """
        if not isinstance(surname, str):
            raise TypeError("argument is not a string")
        if not surname:
            raise ValueError("wrong value")
        self.__surname = surname

    def setMobilePhone(self, mobile_phone):
        """ Sets mobile phone. """
        if not isinstance(mobile_phone, str):
            raise TypeError("argument is not a string")
        if not len(mobile_phone) == 10 or not re.match(r'[0][0-9]{9}', mobile_phone):
            raise ValueError("wrong value")
        self.__mobile_phone = mobile_phone

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
        """ Initializes variables. """
        self.setCustomer(customer)
        self.setProducts(products)

    def setCustomer(self, customer):
        """ Sets customer. """
        if not isinstance(customer, Customer):
            raise TypeError("argument is not a customer")
        self.__customer = customer

    def setProducts(self, products):
        """ Sets products"""
        if not isinstance(products, list) or not all(isinstance(x, Product) for x in products):
            raise TypeError("argument is not a list of products")
        self.__products = products

    def getTotalPrice(self):
        """ Counts and returns total price. """
        total_prise = 0
        for i in range(len(self.__products)):
            total_prise += self.__products[i].getPrice()
        return total_prise

    def addProduct(self, product):
        """ Adds a product. """
        if not isinstance(product, Product):
            raise TypeError("argument is not a product")
        self.__products.append(product)

    def delProduct(self, product):
        """ Removes the product. """
        if not isinstance(product, Product):
            raise TypeError("argument is not a product")
        self.__products.remove(product)


try:
    prod1 = Product(1, "first_product", 1)
    prod2 = Product(2, "second_product", 2)
    prod3 = Product(3, "third_product", 3)
    cust = Customer("Sergey", "Kurnosenko", "0951713987")
    ord = Order(cust, [prod1, prod2])
    ord.addProduct(prod3)
    ord.delProduct(prod2)
    print("total price = ", ord.getTotalPrice())
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
