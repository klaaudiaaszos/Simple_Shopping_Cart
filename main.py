from cart import *

phone1 = Phone ("iPhone 15", 2355, "blue")
tv1 = TV ("Samsung Crystal UHD", 2500, 65)

cart = Cart ()
cart.addProduct (phone1)
cart.addProduct (tv1)
cart.addProduct (tv1)
cart.addProduct ("test")
print (cart)