#SINGLE LEVEL INHERITANCE
#parent class
class Parent:
    i = 5
    def fun1(self):
        print('Hey there, you are in the parent class')

#subclass
class Child(Parent):
    i=10
    def fun2(self):
        print('Hey there, you are in the sub class')
temp1=Child()
temp2=Parent()
temp1.fun1()
temp1.fun2()
temp2.fun1()
print(temp1.i)
print(temp2.i)
#temp2.fun2()