import math


class Calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
# print(self.a)

c = Calculator(6, 3)
print("Add:", c.add(), " Subtract:", c.subtract(), " Multiply:", c.multiply(), " Divide:", c.divide())

# inheritance was used
class ScienceCalculator(Calculator): 
    def __init__(self, a, b):
        super().__init__(a, b)

    def exp(self):
        return self.a**self.b
    
    def log(self):
        return math.log( self.a, self.b )
    
    def divide(self):
        if self.b ==0:
            return None
    

sc = ScienceCalculator(16,2)
testDivideByZero = ScienceCalculator(2,0)
print("Add:", sc.add(), " Exponential:", sc.exp(), " Logarithm:", sc.log(), " Divide:", testDivideByZero.divide()) 


# test cases
c = Calculator(2,3)
assert c.add() == 5

c = Calculator(5,3)
assert c.add() == 8

c = Calculator(112,15)
assert c.add() == 127

