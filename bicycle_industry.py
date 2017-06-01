#here we attempt to create a simple model of the bicycle industry
#as outlined in unit 1 lesson 3

class Wheel(object):
    def __init__(self,wheel_type):
        
        #wheel data lists name, weight (kg) and cost
        #for each wheel type
        wheel_data = {"a":["el cheapo",1,30], 
                      "b":["classic",1.5,55],
                      "c":["royal",0.75,120]
                     }
        self.wheel_type = wheel_type 
        self.name = wheel_data[wheel_type][0]
        self.weight = wheel_data[wheel_type][1]
        self.cost = wheel_data[wheel_type][2]
    
    #accessors        
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def get_cost(self):
        return self.cost
        
class Frame(object):
    def __init__(self,frame_type):
        
        #wheel data lists name, weight (kg) and cost
        #for each frame type
        frame_data = {"a":["woody",17,50],
                      "b":["steely",15,150],
                      "c":["carbon-fibery",8,900]
                     }
        self.frame_type = frame_type 
        self.name = frame_data[frame_type][0]
        self.weight = frame_data[frame_type][1]
        self.cost = frame_data[frame_type][2]
    
    #accessors        
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def get_cost(self):
        return self.cost
        
class Bicycle(object):
    def __init__(self, name, wheels, frame):
        self.name = name
        self.wheels = wheels
        self.frame = frame
        self.weight = (wheels[0].get_weight() + 
                       wheels[1].get_weight() +
                       frame.get_weight())
        self.cost = (wheels[0].get_cost() + 
                     wheels[1].get_cost() +
                     frame.get_weight())
    #accessors  
    def get_name(self):
        return self.name
    def get_frame(self):
        return self.frame
    def get_wheels(self):
        return self.wheels
    def get_weight(self):
        return self.weight
    def get_cost(self):
        return self.cost

class Bikeshop(object):
    def __init__(self,name):
        self.name=name
        self.inventory=[]
        self.margin = 0.2
        self.profit = 0
    
    #method of sellinf bicycle to customer
    def sell(self, bicycle, customer):
        price = bicycle.get_cost*(1+self.margin)
        #customer.buy returns true if they can afford it
        if customer.buy(bicycle,price):
            #update profit leger
            self.profit = self.profit + bicycle.get_cost * self.margin
            #use list comprehension to remove from inventory
            self.inventory = [unit for unit in self.inventory 
                              if unit is not bicycle]
                              
    #method for adding bicycle to inventory
    def stock(self, bicycle):
        self.inventory.append(bicycle)
    #accessors
    def get_name(self):
        return self.name
    def get_profit(self):
        return self.profit
    def get_inventory(self):
        return self.inventory
            
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
                  bicycle.get_name + " for " +
                  str(price))
            return True
        else:
            print("can't afford it")
            return False
            
    #accessors   
    def get_name(self):
        return self.name
    def get_budget(self):
        return self.budget
    def get_owned_bikes(self):
        return self.owned_bikes


###THIS IS OUR "MAIN" TESTING METHOD FOR NOW
if __name__ == '__main__':
    
    #create bike instances to stock our shop
    n1 = Wheel("a")
    n2 = Wheel("a")
    nf = Frame("a")
    the_neptune = Bicycle("the_neptune", [n1, n2], nf)
    
    b1 = Wheel("a")
    b2 = Wheel("a")
    bf = Frame("a")
    the_badger = Bicycle("the_badger", [b1, b2], bf)
    
    w1 = Wheel("b")
    w2 = Wheel("b")
    wf = Frame("b")
    the_winston = Bicycle("the_winston", [w1, w2], wf)
    
    s1 = Wheel("b")
    s2 = Wheel("b")
    sf = Frame("b")
    the_stanley = Bicycle("the_stanley", [s1, s2], sf)
    
    r1 = Wheel("c")
    r2 = Wheel("c")
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
    
    
    
    bob = Customer("Bob", 1000)
    joe = Customer("Joe",500)
    ted = Customer("Ted",200)
    

    
    
    print(str(the_neptune.get_name()))
    print(the_neptune.get_weight())
    print(the_neptune.get_cost())
    
    
    
    