from tkinter import *
operator = 'none'

# # Window widget
root = Tk()
root.title("Simple Calculator!")

e = Entry(root, width = 15, borderwidth= 5, font = ("Times", "24", "bold italic"))
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def Button_Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def Button_Clear():
    e.delete(0, END)
    return

def Button_Add():
    global first_number
    global operator
    
    first_number = e.get()
    first_number = str(first_number)
    e.delete(0, END)
    operator = 'add'
    return

def Button_Subtract():
    global first_number
    global operator
    
    first_number = e.get()
    first_number = str(first_number)
    e.delete(0, END)
    operator = 'sub'
    return

def Button_Divide():
    global first_number
    global operator
    
    first_number = e.get()
    first_number = str(first_number)
    e.delete(0, END)
    operator = 'div'
    return

def Button_Multiply():
    global first_number
    global operator
    
    first_number = e.get()
    first_number = str(first_number)
    e.delete(0, END)
    operator = 'mult'
    return

def Button_Equal():
    Second_number = e.get()
    global operator
    if operator == 'none':
        e.delete(0, END)
        out = str(Second_number)
    elif operator == 'add':
        e.delete(0, END)
        out = str(int(first_number)+int(Second_number))
    elif operator == 'sub':
        e.delete(0, END)
        out = str(int(first_number)-int(Second_number))
    elif operator == 'mult':
        e.delete(0, END)
        out = str(int(first_number)*int(Second_number))
    elif operator == 'div':
        e.delete(0, END)
        out = str(int(first_number)/int(Second_number))
    e.insert(0, out)
    operator = 'none'
    return

myButton_7 = Button(root, text = '7',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(7) , 
                    padx = 10, pady = 0).grid(row = 1, column = 0)
myButton_8 = Button(root, text = '8',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(8) , 
                    padx = 10, pady = 0).grid(row = 1, column = 1)
myButton_9 = Button(root, text = '9',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(9) , 
                    padx = 10, pady = 0).grid(row = 1, column = 2)
myButton_add = Button(root, text = '  +  ',font = ("Times", "24", "bold italic"), command = lambda: Button_Add() , 
                      padx = 10, pady = 0,width = 5).grid(row = 1, column = 3) 

myButton_4 = Button(root, text = '4',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(4) , 
                    padx = 10, pady = 0).grid(row = 2, column = 0)
myButton_5 = Button(root, text = '5',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(5) , 
                    padx = 10, pady = 0).grid(row = 2, column = 1)
myButton_6 = Button(root, text = '6',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(6) , 
                    padx = 10, pady = 0).grid(row = 2, column = 2)
myButton_subtract = Button(root, text = '  -  ',font = ("Times", "24", "bold italic"), command = lambda: Button_Subtract(), 
                           padx = 10, pady = 0,width = 5).grid(row = 2, column = 3)

myButton_1 = Button(root, text = '1',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(1) , 
                    padx = 10, pady = 0).grid(row = 3, column = 0)
myButton_2 = Button(root, text = '2',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(2), 
                    padx = 10, pady = 0).grid(row = 3, column = 1)
myButton_3 = Button(root, text = '3',font = ("Times", "24", "bold italic"), command = lambda: Button_Click(3), 
                    padx = 10, pady = 0).grid(row = 3, column = 2)
myButton_Clear = Button(root, text = 'Clear',font = ("Times", "24", "bold italic"), command = lambda: Button_Clear(), 
                        padx = 10, pady = 0,width = 5).grid(row = 3, column = 3)

myButton_0 = Button(root, text = '0', font = ("Times", "24", "bold italic"), command = lambda: Button_Click(0), 
                    padx = 10, pady = 0).grid(row = 4, column = 0)
myButton_multiply = Button(root, text = '*', font = ("Times", "24", "bold italic"), command = lambda: Button_Multiply(), 
                           padx = 10, pady = 0).grid(row = 4, column = 1)
myButton_divide = Button(root, text = ' /', font = ("Times", "24", "bold italic"), command = lambda: Button_Divide(), 
                         padx = 10, pady = 0).grid(row = 4, column = 2)
myButton_equal = Button(root, text = '=', font = ("Times", "24", "bold italic"), command = lambda: Button_Equal(), 
                        padx = 10, pady = 0, width = 5).grid(row = 4, column = 3)

root.mainloop()