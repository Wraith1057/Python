'''
Create a class called Numbers, which has a single class
attribute called MULTIPLIER,
and a constructor which takes the
parameters x and y (these should all be numbers).
'''
class Numbers:
    MULTIPLIER = 3.5
    def __init__(self, x, y):#instance/ constructor
        self.x = x
        self.y = y
    #instance method
    def add(self):
        return self.x + self.y
    #@classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a
    #@staticmethod
    def subtract(b, c):
        return b - c
t=Numbers(2,4)
print(t.add())#6
print(t.multiply(2))#3.5*2=7
print(Numbers.subtract(4,3))#1
