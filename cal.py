from tkinter import *

window = Tk()
window.title('Calculator') 
window.geometry("400x350") 
window.resizable(False, False) 

def Add():
    sum = float(num1.get()) + float(num2.get())
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(sum))

def Diff():
    diff = float(num1.get()) - float(num2.get())
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(diff))

def Mul():
    mul = float(num1.get()) * float(num2.get())
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(mul))

def Div():
    div = float(num1.get()) / float(num2.get())
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(div))

mainTitle = Label(window, text="Simple Calculator",fg="green", font=("Arial", 25))
mainTitle.place(x=75, y=25) 

num1_label = Label(window, text="Type Value 1:", font=("Arial", 15))
num1_label.place(x=60, y=100)
num1 = Entry(window)
num1.place(x=200, y=104, height=25, width=143)
num2_label = Label(window, text="Type Value 2:", font=("Arial", 15))
num2_label.place(x=61, y=150)
num2 = Entry(window)
num2.place(x=200, y=154, height=25, width=143)
resultLabel = Label(window, text="Result:", font=("Arial", 15))
resultLabel.place(x=118, y=206)
resultEntry = Entry(window)
resultEntry.place(x=200, y=210, height=25, width=143)

buttonAdd = Button(window, text="+", fg="white", bg="green", font=("Arial", 16), command=Add) 
buttonAdd.place(x=74, y=262, height=32, width=56)
buttonSub = Button(window, text="-", fg="white", bg="green", font=("Arial", 16), command=Diff)
buttonSub.place(x=142, y=262, height=32, width=56)
buttonMul = Button(window, text="x", fg="white", bg="green", font=("Arial", 16), command=Mul)
buttonMul.place(x=210, y=262, height=32, width=56)
buttonDiv = Button(window, text="/", fg="white", bg="green", font=("Arial", 16), command=Div) 
buttonDiv.place(x=278, y=262, height=32, width=56)

window.mainloop()
