from tkinter import *
root=Tk()

x=Label(root,text="Create a New Account").grid(row=0,columnspan=5)

a1=Label(root,text="First Name").grid(row=1,column=1)
a2=Entry(root,bd=3)
a2.grid(row=1,column=2)

b1=Label(root,text="Last Name").grid(row=2,column=1)
b2=Entry(root,bd=3)
b2.grid(row=2,column=2)

c1=Label(root,text="Email Address").grid(row=3,column=1)
c2=Entry(root,bd=3)
c2.grid(row=3,column=2)

d1=Label(root,text="Password").grid(row=4,column=1)
d2=Entry(root,bd=3,show="*")
d2.grid(row=4,column=2)

e1=Label(root,text="Enter Otp").grid(row=5,column=1)
e2=Entry(root,bd=3)
e2.grid(row=5,column=2)

f1=tkinter.Button(root,text="verify otp",relief=RAISED).grid(row=5,column=3)
def clean():
    a2.delete(0,'end')
    b2.delete(0,'end')
    c2.delete(0,'end')
    d2.delete(0,'end')
    e2.delete(0,'end')
g1=Button(root,text="Clear",relief=RAISED,command=clean).grid(row=6,column=1)
def register():
    print("First Name:-",a2.get())
    print("Last Name:-",b2.get())
    print("Email Address:-",c2.get())
    print("Password:-",d2.get())
    print("Entered Otp:-",e2.get())
g2=Button(root,text="Register",relief=RAISED,command=register).grid(row=6,column=2)
def exit1():
    root.destroy()
g3=Button(root,text="Exit",relief=RAISED,command=exit1).grid(row=6,column=3)