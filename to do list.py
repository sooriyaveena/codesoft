import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq

root = tk.Tk()
root.title('TO DO LIST')
root.geometry("400x250+500+300")

conn = sq.connect('tasks_db.db')
cur = conn.cursor()
cur.execute('create table if not exists tasks (name text)')

tasks = []


def addTask():
    new_task = entry.get()
    if len(new_task) == 0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        tasks.append(new_task)
        cur.execute('insert into tasks values (?)', (new_task,))
        updateList()
        entry.delete(0, 'end')


def updateList():
    clearList()
    for task_item in tasks:
        task_list.insert('end', task_item)


def deleteTask():
    try:
        selected_task = task_list.get(task_list.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            updateList()
            cur.execute('delete from tasks where name = ?', (selected_task,))
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')


def deleteAll():
    user_confirm = messagebox.askyesno('Delete All', 'Are you sure?')
    if user_confirm:
        while len(tasks) != 0:
            tasks.pop()
        cur.execute('delete from tasks')
        updateList()


def clearList():
    task_list.delete(0, 'end')


def exitApp():
    print(tasks)
    root.destroy()


def retrieveFromDB():
    while len(tasks) != 0:
        tasks.pop()
    for row in cur.execute('select name from tasks'):
        tasks.append(row[0])


label_heading = ttk.Label(root, text='Task Manager')
label_instruction = ttk.Label(root, text='Enter task name: ')
entry = ttk.Entry(root, width=21)
task_list = tk.Listbox(root, height=11, selectmode='SINGLE')
button_add = ttk.Button(root, text='Add Task', width=20, command=addTask)
button_delete = ttk.Button(root, text='Delete Task', width=20, command=deleteTask)
button_delete_all = ttk.Button(root, text='Delete All', width=20, command=deleteAll)
button_exit = ttk.Button(root, text='Exit', width=20, command=exitApp)

retrieveFromDB()
updateList()

label_instruction.place(x=50, y=50)
entry.place(x=50, y=80)
button_add.place(x=50, y=110)
button_delete.place(x=50, y=140)
button_delete_all.place(x=50, y=170)
button_exit.place(x=50, y=200)
label_heading.place(x=50, y=10)
task_list.place(x=220, y=50)

root.mainloop()

conn.commit()
cur.close()