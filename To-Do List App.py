from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="whitesmoke")

# For showing earlier tasks on listbox-
def previous_task():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                lbx.insert(END, line.strip())
    except FileNotFoundError:
        open("tasks.txt", "w").close() # create file if not exists-

# Adding tasks on file & listbox
def add_item():
    try:
        task = item_entry.get()
        with open("tasks.txt","a") as f:
            f.write(task+"\n")
            f.close()
        lbx.insert(END, task)
        item_entry.delete(0, END)

    except ValueError :
        tmsg.showerror("Error", "Something went wrong")

# Deleting selected tasks from file & listbox-
def del_task():
        index=lbx.curselection()
        if index:
            task_text=lbx.get(index[0])
            lbx.delete(index[0])
            try:
                with open("tasks.txt", "r") as f:
                    lines = f.readlines()
                with open("tasks.txt", "w") as f:
                    for line in lines:
                        if line.strip() != task_text.strip():
                            f.write(line)
            except FileNotFoundError:
                tmsg.showerror("Error", "Tasks file not found")

        else:
            tmsg.showwarning("Warning", "Please select a task first!")

# Empty - File & listbox-
def clear():
    if tmsg.askyesno("Confirm", "Do you want to clear all tasks?"):
        open("tasks.txt","w").close() # for deleting all data from file-
        lbx.delete(0, END)
        item_entry.delete(0, END)


heading = Label(root, text="Things To Do (Add here)", font=("Arial", 16, "bold"), bg="whitesmoke")
heading.grid(row=0, column=0,columnspan=3,pady=10)

item_entry=Entry(root, font=("lucida", 10),bg="ghostwhite",width=30)
item_entry.grid(row=1,column=0, pady=10,sticky=W,padx=10,ipadx=5)
add_button=Button(root,text="Add Task",command=add_item, bg="seagreen", fg="white", width=10,font=("Arial", 12, "bold"))
add_button.grid(row=1, column=1, pady=10,ipadx=5)

# Created a frame so that we wil work on pack inside frame (can't use grid & pack in 1 place).
frame=Frame(root)
frame.grid(row=2,column=0,padx=20,pady=20)
scrollbar=Scrollbar(frame)
scrollbar.pack(side="right",fill="y",expand=True)
lbx=Listbox(frame, font=("Arial", 10, "bold"),bg="snow",yscrollcommand=scrollbar.set)
lbx.pack(pady=10,padx=10)
scrollbar.config(command=lbx.yview)

Button(root,text="Delete Task",command=del_task,bg="#f44336", fg="white", width=10,font=("Arial", 12, "bold")).grid(row=2,column=1,padx=10,pady=10)
Button(root,text="Clear All",  command=clear,bg="lightblue", fg="black", width=10,font=("Arial", 12, "bold")).grid(row=3,column=0,padx=10,pady=10)

# For calling previous tasks always-
previous_task()

root.mainloop()