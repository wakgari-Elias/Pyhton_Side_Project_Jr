import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do-List")
root.geometry("400x550+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile: 
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", 'r') as taskfile:  
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()  
            if task:
                task_list.append(task)
                listbox.insert(END, task)
    except:
        with open("tasklist.txt", 'w') as taskfile:
            pass 

def deleteTask():
    try:
        selected_task_index = listbox.curselection()[0]
        task_to_remove = listbox.get(selected_task_index)
        task_list.remove(task_to_remove)
        listbox.delete(selected_task_index)

        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# GUI Icon
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

# Top Bar
TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

# Main Input Frame
frame = Frame(root, width=400, height=40, bg="white")
frame.place(x=0, y=140)

task = StringVar()
task_entry = Entry(frame, width=15, font="arial 20", bd=0, fg="#32405b")
task_entry.place(x=10, y=2)
task_entry.focus()

add_button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

# Listbox with Scrollbar
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(100, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height=12, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Open tasks from the file
openTaskFile()

# Delete Button with Image
delete_button = Button(root, text="Delete", font="arial 12 bold", bg="#ff4d4d", fg="white", command=deleteTask)
delete_button.pack(side=BOTTOM, pady=20)

root.mainloop()
