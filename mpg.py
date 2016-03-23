from tkinter import *           # Importing the GUI library
from sympy import *             # Importing the graphing library
from sympy.solvers import solve
from sympy import Symbol

canvas = Tk()                     # Creates a background window
canvas.geometry("1424x840+0+0")
canvas.title("Solve any polynomial equation(s):")

canvas.answer = 0
canvas.first = 0
canvas.second = 0
canvas.equation = ""

#The input boxes
canvas.one = Entry(canvas, bd = 10,width = 10)
canvas.one.place(x = 550, y = 150)

canvas.two = Entry(canvas, bd = 10,width = 10)
canvas.two.place(x = 800, y = 150)

def sum():
    #Textbox for the answer:
    canvas.first = canvas.one.get()
    canvas.second = canvas.two.get()
    canvas.answer = int(canvas.first) + int(canvas.second)
    #Create a label for the asnwer
    Sum = Label(canvas, text = "The answer is: " + str(canvas.answer), font = 20)
    Sum.place(x = 650, y = 450)

#Add Button
Add = Button(canvas, text = 'Add',font = 15,width = 10,
    activebackground = "grey", command = sum)
Add.place(x = 400,y = 300)

def difference():

    #Textbox for the answer:
    canvas.first = canvas.one.get()
    canvas.second = canvas.two.get()
    canvas.answer = int(canvas.first) - int(canvas.second)
    #Create a label for the asnwer
    Difference = Label(canvas, text = "The answer is: " + str(canvas.answer), font = 20)
    Difference.place(x = 650, y = 450)


#Subtract Button
Sub = Button(canvas, text = 'Subtract',font = 15,width = 10,
    activebackground = "grey", command = difference)
Sub.place(x = 600,y = 300)

def product():
    
    #Textbox for the answer:
    canvas.first = canvas.one.get()
    canvas.second = canvas.two.get()
    canvas.answer = int(canvas.first) * int(canvas.second)
    #Create a label for the asnwer
    Product = Label(canvas, text = "The answer is: " + str(canvas.answer), font = 20)
    Product.place(x = 650, y = 450)


#Multiply Button
Sub = Button(canvas, text = 'Multiply',font = 15,width = 10,
    activebackground = "grey", command = product)
Sub.place(x = 800,y = 300)

def quotient():
    
    #Textbox for the answer:
    canvas.first = canvas.one.get()
    canvas.second = canvas.two.get()
    canvas.answer = int(canvas.first) / int(canvas.second)
    #Create a label for the asnwer
    Quotient = Label(canvas, text = "The answer is: " + str(canvas.answer), font = 20)
    Quotient.place(x = 650, y = 450)


#Divide Button
Sub = Button(canvas, text = 'Divide',font = 15,width = 10,
    activebackground = "grey", command = quotient)
Sub.place(x = 1000,y = 300)


#Equation input box
canvas.eq = Entry(canvas, bd = 10,width = 30)
canvas.eq.place(x = 625, y = 600)


def solved():
    canvas.three = 3
    x = Symbol('x')
    canvas.solved = canvas.eq.get()
    equat = str(canvas.solved)
    canvas.solved = solve(str(canvas.solved), x)
    roots = Label(canvas, text = "x =  " + str(canvas.solved), font = 20)
    roots.place(x = 450, y = 675)

#Solve Button
Solve = Button(canvas, text = 'Solve',font = 15,width = 10,
    activebackground = "grey", command = solved)
Solve.place(x = 1000,y = 600)

#Text Plus Sign
Plus = Label(canvas, text = "+ - * /", font = 20)
Plus.place(x = 690, y = 155)

