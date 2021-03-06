# strategy.py

import types

class Strategy:
    """The Strategy Pattern class"""
    
    def __init__(self, function=None):
        self.name = "Default Strategy"        
            
    def execute(self):
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

#Method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

#Method 2    
def strategy_two(self):
	print("{} is used to execute method 2".format(self.name))
    

#Let's create our default strategy
s0 = Strategy()
#Let's execute our default strategy
s0.execute()
#Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
#Let's set its name
s1.name = "Strategy One"
#Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
