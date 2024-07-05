#HIERARCHICAL INHERITANCE
#parent class
class Parent:
    def fun1(self):
        print('Hey there, you are in the parent class')
#child class 1
class child1(Parent):
    def fun2(self):
        print('Hey there, you are in the child class 1')
#child class 2 
class child2(Parent):
    def fun3(self):
        print('Hey there, you are in the child class 2')
#child class 3
class child3(Parent):
    def fun4(self):
        print('Hey there, you are in the child class 3')
# main program
obj1 = child3()
obj2 = child2()
obj3 = child1()
obj1.fun1()
obj1.fun4()
obj2.fun1()
obj2.fun3()
obj3.fun1()
obj3.fun2()