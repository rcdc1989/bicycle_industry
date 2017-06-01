#here we attempt to create a simple model of the bicycle industry
#as outlined in unit 1 lesson 3

class Wheel(object):
    def __init__(self,wheel_type):
        
        #wheel data lists name, weight (kg) and cost
        #for each wheel type
        wheel_data = {"a":["el cheapo",1,30], 
                      "b":["classic",1.5,90],
                      "c":["royal",0.75,120]
                     }
        self.wheel_type = wheel_type 
        self.name = wheel_data[wheel_type][0]
        self.weight = wheel_data[wheel_type][1]
        self.cost = wheel_data[wheel_type][2]
    
class Frame(object):
    def __init__(self,frame_type):
        
        #wheel data lists name, weight (kg) and cost
        #for each frame type
        frame_data = {"a":["woody",17,50],
                      "b":["steely",15,150],
                      "c":["carbon-fibery",8,500]
                     }
        self.frame_type = frame_type 
        self.name = frame_data[frame_type][0]
        self.weight = frame_data[frame_type][1]
        self.cost = frame_data[frame_type][2]
    
class Bicycle(object):
    def __init__(self, name, wheels, frame):
        self.name = name
        self.wheels = wheels
        self.frame = frame
        self.weight = (wheels[0].weight+ 
                       wheels[1].weight+
                       frame.weight)
        self.cost = (wheels[0].cost + 
                     wheels[1].cost +
                     frame.cost)

class Bikeshop(object):
    def __init__(self,name):
        self.name=name
        self.inventory=[]
        self.margin = 0.2
        self.profit = 0
    
    #method of sellinf bicycle to customer
    def sell(self, bicycle, customer):
        price = bicycle.cost*(1+self.margin)
        #customer.buy returns true if they can afford it
        if customer.buy(bicycle,price):
            #update profit leger
            self.profit = self.profit + bicycle.cost * self.margin
            #use list comprehension to remove from inventory list
            self.inventory = [unit for unit in self.inventory 
                              if unit is not bicycle]
                              
    def gen_selection(self):
        selection = []
        for bike in self.inventory:
            price = bike.cost*(1+self.margin)
            selection.append([bike,price])
        return selection
        
    def gen_budget_selection(self,budget):
        selection = []
        for bike in self.inventory:
            price = bike.cost*(1+self.margin)
            if price <= budget:
                selection.append([bike,price])
        return selection
                              
    #method for adding bicycle to inventory
    def stock(self, bicycle):
        self.inventory.append(bicycle)
            
class Customer(object):
    def __init__(self,name, budget):
        self.name = name
        self.budget = budget
        self.owned_bikes = []
        
    def buy(self,bicycle,price):
        
        if self.budget >= price:
            self.budget = self.budget - price
            self.owned_bikes.append(bicycle)
            print(str(self.name) + " bought " +
                  bicycle.name + " for " +
                  str(price))
            return True
        else:
            print("can't afford it")
            return False


###THIS IS OUR "MAIN" TESTING METHOD FOR NOW
if __name__ == '__main__':
    
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
    

    
    
##
#REMOVE accessors
#create retail_price attribute for each bicycle
    