import math

#CONSTANTS
LEARNIG_RATE = 0.5

# FORMULAS
class Formulas:
    
    def sigmoid (self, x:float):
            return 1 / (1 + math.exp(-x))
    
    def summation(self, function, elements:list):
        
        if callable(function):
            try:
                return sum(function(i) for i in elements)
            except:
                 raise ValueError("Parameters not appropriate for the function")
        else:
            raise TypeError("The input is not a valid function")
    



_init = Formulas()
sigmoid = _init.sigmoid
summation = _init.summation


        

