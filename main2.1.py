import numbers


class Product:
    def __init__(self, price, description, dimensions):
        if (isinstance(price, numbers.Number) and isinstance(description, str)
                and isinstance(dimensions, numbers.Number)):
            self.__price = price
            self.__description = description
            self.__dimensions = dimensions
        else:
            raise TypeError("wrong arguments")

    def getPrice(self):
        return self.__price


class Customer:
    def __init__(self, name, surname, mobile_phone):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(mobile_phone, str):
            self.__name = name
            self.__surname = surname
            self.__mobile_phone = mobile_phone
        else:
            raise TypeError("wrong arguments")

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getMobilePhone(self):
        return self.__mobile_phone


class Order:
    def __init__(self, customer, products):
        if (isinstance(products, list) and all(isinstance(x, Product) for x in products)
                and isinstance(customer, Customer)):
            self.__customer = customer
            self.__products = products
        else:
            raise TypeError("wrong arguments")

    def getTotalPrice(self):
        total_prise = 0
        for i in range(len(self.__products)):
            print("a",total_prise)
            total_prise += self.__products[i].getPrice()
        return total_prise


try:
    p1 = Product(1, "asd", 2)
    p2 = Product(4, "asd", 3)
    c = Customer("Sergey", "Kurnosenko", "88005553535")
    o = Order(c, [p1, p2])
    print("total price = ", o.getTotalPrice())
except TypeError as e:
    print(e)
