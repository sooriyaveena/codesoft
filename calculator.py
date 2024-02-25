from tkinter import *

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


root = Tk()
root.title("Simple Calculator")
root.configure(bg="black")  
entry = Entry(root, width=35, borderwidth=5, bg="white")  
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for (text, row, col) in buttons:
    if text == '=':
        button = Button(root, text=text, padx=20, pady=10, bg="black", fg="white", command=calculate) 
    else:
        button = Button(root, text=text, padx=20, pady=10, bg="black", fg="white", command=lambda t=text: entry.insert(END, t)) 
    button.grid(row=row, column=col)


clear_button = Button(root, text="Clear", padx=60, pady=10, bg="black", fg="white", command=lambda: entry.delete(0, END))  
clear_button.grid(row=5, column=0, columnspan=4)


root.mainloop()
