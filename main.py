from bicycle_industry import *

#create bike instances to stock our shop
n1 = Wheel("a")
n2 = Wheel("a")
nf = Frame("a")
#the_neptune = Bicycle("the_neptune", [n1, n2], nf)
the_neptune = Bicycle("the_neptune", [Wheel("a"), Wheel("a")], Frame("a"))

b1 = Wheel("b")
b2 = Wheel("b")
bf = Frame("a")
the_badger = Bicycle("the_badger", [b1, b2], bf)

w1 = Wheel("b")
w2 = Wheel("b")
wf = Frame("b")
the_winston = Bicycle("the_winston", [w1, w2], wf)

s1 = Wheel("c")
s2 = Wheel("c")
sf = Frame("b")
the_stanley = Bicycle("the_stanley", [s1, s2], sf)

r1 = Wheel("b")
r2 = Wheel("b")
rf = Frame("c")
the_rolls = Bicycle("the_rolls", [r1, r2], rf)

q1 = Wheel("c")
q2 = Wheel("c")
qf = Frame("c")
the_queen = Bicycle("the_queen", [q1, q2], qf)

#instantiate a shop and stock it with the bikes we created
a_shop = Bikeshop("a_shop")
a_shop.stock(the_queen)
a_shop.stock(the_rolls)
a_shop.stock(the_stanley)
a_shop.stock(the_winston)
a_shop.stock(the_badger)
a_shop.stock(the_neptune)

#we use a loop to print available selection
for item in a_shop.gen_selection():

    print(item[0].name + " .... " + str(item[1]) +"$")

#instantiate some customers
bob = Customer("Bob", 1000)
joe = Customer("Joe",500)
ted = Customer("Ted",200)


#print a list for what each customer can afford
print("\n \nBob can afford the following:")
for item in a_shop.gen_budget_selection(bob.budget):

    print(item[0].name + " .... " + str(item[1]) +"$")

print("\n \nJoe can afford the following:")
for item in a_shop.gen_budget_selection(joe.budget):

    print(item[0].name + " .... " + str(item[1]) +"$")
    
print("\n \nTed can afford the following:")
for item in a_shop.gen_budget_selection(ted.budget):

    print(item[0].name + " .... " + str(item[1]) +"$")