from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

window = Tk()

window.title("TODO")

def entertask():
        input_text=entry_task.get()
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please enter the text")
        else:
            listbox_task.insert(tkinter.END,input_text)
        entry_task.delete(0,tkinter.END)
    

def deletetask():
        selected=listbox_task.curselection()
        listbox_task.delete(selected[0])

def markasdone():
        marked=listbox_task.curselection()
        temp=marked[0]

        temp_marked=listbox_task.get(marked)

        temp_marked=temp_marked+"✔"

        listbox_task.delete(temp)
        listbox_task.insert(temp,temp_marked)

frame_task = Frame(window)
frame_task.pack()


listbox_task = Listbox(frame_task,bg="lightblue",fg="black",height=15,width=50,font="serif")
listbox_task.pack(side=tkinter.LEFT)

entry_task=tkinter.Entry(window,width=50)
entry_task.pack()


#to scroll the list 
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#buttons to add , delete, mark as done .
entry_button=Button(window,text="Add task",width=60,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete task",width=60,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as done",width=60,command=markasdone)
mark_button.pack(pady=3)



window.mainloop()