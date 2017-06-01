#here we attempt to create a simple model of the bicycle industry
#as outlined in unit 1 lesson 3

class Wheel(object):
    def __init__(self,wheel_type):
        
        #wheel data lists name, weight (kg) and cost
        #for each wheel type
        wheel_data = {"a":["el cheapo",1,10], 
                      "b":["classic",1.5,25],
                      "c":["royal",0.75,100]
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
                      "b":["steely",15,75],
                      "c":["carbon-fibery",8,300]
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
        self.sales = 0
    
    #accessors
    def get_name(self):
        return self.name
        
    def sell(self,bicycle,customer):
        if customer.get_budget
        
class Customer(object):
    def __init__(self,name, budget):
        self.name = name
        self.budget = budget
        self.owned_bikes = []
        
    def buy(self,bicyle,price):
        
    
    #accessors   
    def get_name(self):
        return self.name
    def get_budget(self):
        return self.budget
    def get_owned_bikes(self):
        return self.owned_bikes


if __name__ == '__main__':
    
    #create instances of our objects
    n1 = Wheel("a")
    n2 = Wheel("a")
    nf = Frame("a")
    the_neptune = Bicycle("the_neptune", [n1, n2], nf)
    
    w1 = Wheel("b")
    w2 = Wheel("b")
    wf = Frame("b")
    the_winston = Bicycle("the_winston", [w1, w2], wf)
    
    r1 = Wheel("c")
    r2 = Wheel("c")
    rf = Frame("c")
    the_rolls = Bicycle("the_rolls", [r1, r2], rf)
    
    bob = Customer("bob", 1000)

    a_shop = Bikeshop("a_shop")
    
    print(str(the_neptune.get_name()))
    print(the_neptune.get_weight())
    print(the_neptune.get_cost())
    
    
    
    