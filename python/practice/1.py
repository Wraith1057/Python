class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def Name(self):
        return self.firstname + " " + self.lastname
class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)#to access constructor of parent class
        Person.Name(self)
        self.staffnumber = staffnum
    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber
x = Person("Nitesh", "Shukla")
y = Employee("Brijesh", "Shukla", "1001")

print(x.Name())
print(y.Name())
print(y.GetEmployee())
print(x.GetEmployee())