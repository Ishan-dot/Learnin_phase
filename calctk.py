from tkinter import *
import tkinter as tk
w= tk.Tk()
w.title('Calculator')
w.geometry('200x200')

w.config(background='black')
def add():
    n1= int(num1.get())
    n2= int(num2.get())
    result.config(text=f'Output:{n1+n2}')

num1=tk.Entry(w)
num1.pack()
num2=tk.Entry(w)
num2.pack()

b=tk.Button(w,text='Add',command=add)
b.pack()
result=tk.Label(w, text='Output')
result.pack()

w.mainloop()