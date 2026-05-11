from products import *

class Cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct (self, product):
        #if isinstance (product, Phone) or isinstance (product, TV):
        if isinstance (product, Product):
            if product not in self.__productsList:
                self.__productsList.append (product)
                self.calculateCart ()

    def calculateCart (self):
        self.__cartValue = 0
        for n in self.__productsList:
            self.__cartValue += n.price

    def __str__(self):
        strData = "\nCart info, products list: "
        for n in self.__productsList:
            strData += "\n - " + str (n.name) + " " + str (n.price) + " PLN"
        strData += "\nCart value: " + str(self.__cartValue) + " PLN"
        return strData

