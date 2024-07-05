#HYBRID 
class A:
    def fun1(self):
        print('Hey there, you are in class A')
class B(A):
    def fun2(self):
        print('Hey there, you are in class B')
class C(A):
    def fun3(self):
        print('Hey there, you are in class C')
class D(C,A):
    def fun4(self):
        print('Hey there, you are in the class D')
#main program
h = D()
h.fun4()
h.fun3()
h.fun1()