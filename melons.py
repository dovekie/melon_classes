"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5.0
        if qty >= 3:
            total = (price * qty) * 0.75
        else:
            total = price * qty

        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        price = 5.0
        if qty >= 5:
            total = (price * qty) * 0.50
        else:
            total = price * qty

        return total    

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        shipping = 1.5
        price = 6.0 * shipping
        total = price * qty

        return total   
bobs_order = CasabaOrder()
print bobs_order.get_price(1) 

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        shipping = 1.5
        price = 5.0 * shipping
        total = price * qty

        return total    

class SantaClausOrder(object):
    species = "Santa_Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        shipping = 1.5
        price = 5.0 * shipping
        total = price * qty

        return total    

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        price = 5.0
        total = price * qty

        return total    

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        shipping = 1.5
        price = 5.0 * shipping
        total = price * qty

        return total    

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        shipping = 1.5
        shape_dif = 2
        price = 5.0 * shipping * shape_dif
        total = price * qty

        return total    

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        price = 6.0
        total = price * qty

        return total