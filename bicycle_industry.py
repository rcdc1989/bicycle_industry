#here we attempt to create a simple model of the bicycle industry
#as outlined in unit 1 lesson 3

class Bicycle(object):
    def __init__(self, name, wheel, frame):
        self.name = name
        self.wheel = wheel
        self.frame = frame
        self.weight = 1 + 2
        self.cost = 3 + 4
        
    def get_name(self):
        return self.name
    def get_frame(self):
        return self.frame
    def get_wheel(self):
        return self.wheel
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
    
    def get_name(self):
        return self.name
        
class Customer(object):
    def __init__(self,name, budget):
        self.name = name
        self.budget = budget
        self.owned_bikes = []
        
    def get_name(self):
        return self.name
        
        
if __name__ == '__main__':
    
    
    #create instances of our objects
    bob = Customer("bob", 1000)
    the_neptune = Bicycle("the_neptune","crazy","weird")
    the_winston = Bicycle("the_winston","expensive","classy")
    the_gargoyle = Bicycle("the_gargoyle","ugly","scary")
    a_shop = Bikeshop("a_shop")
    
    print(str(the_neptune.get_name()))
    print(the_neptune.get_frame())
    print(the_neptune.get_cost())
    
    
    
    