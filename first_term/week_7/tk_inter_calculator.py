import tkinter as tk

def calculate():
    pass

root = tk.Tk()
root.title("Simple Calculator :) ")

label_num1 = tk.Label(root, text = "Enter first number")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text = "Enter second number")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

var_operation = tk.StringVar(root)
var_operation.set('addition')

label_operation = tk.Button