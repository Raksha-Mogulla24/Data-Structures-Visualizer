import tkinter as tk

stack = []
queue = []
linked_list = []
history = []

# ---------- HISTORY ----------
def update_history(action):
    history.append(action)
    history_box.insert(tk.END, action)

# ---------- STACK ----------
def push():
    value = entry.get()
    if value:
        stack.append(value)
        entry.delete(0, tk.END)
        update_history("Push: " + value)
        update_stack()

def pop():
    if stack:
        value = stack.pop()
        update_history("Pop: " + value)
        update_stack()

def update_stack():
    stack_box.delete(0, tk.END)
    for item in reversed(stack):
        stack_box.insert(tk.END, item)

# ---------- QUEUE ----------
def enqueue():
    value = entry.get()
    if value:
        queue.append(value)
        entry.delete(0, tk.END)
        update_history("Enqueue: " + value)
        update_queue()

def dequeue():
    if queue:
        value = queue.pop(0)
        update_history("Dequeue: " + value)
        update_queue()

def update_queue():
    queue_box.delete(0, tk.END)
    for item in queue:
        queue_box.insert(tk.END, item)

# ---------- LINKED LIST ----------
def insert_node():
    value = entry.get()
    if value:
        linked_list.append(value)
        entry.delete(0, tk.END)
        update_history("Insert Node: " + value)
        update_linked_list()

def delete_node():
    if linked_list:
        value = linked_list.pop()
        update_history("Delete Node: " + value)
        update_linked_list()

def update_linked_list():
    list_box.delete(0, tk.END)
    for item in linked_list:
        list_box.insert(tk.END, item)

# ---------- GUI ----------
window = tk.Tk()
window.title("Data Structures Visualizer")
window.geometry("600x650")

title = tk.Label(window, text="Data Structures Visualizer", font=("Arial",18))
title.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Stack
tk.Label(window,text="Stack",font=("Arial",14)).pack()
tk.Button(window,text="Push",command=push).pack()
tk.Button(window,text="Pop",command=pop).pack()

stack_box = tk.Listbox(window,height=6,width=25)
stack_box.pack(pady=5)

# Queue
tk.Label(window,text="Queue",font=("Arial",14)).pack()
tk.Button(window,text="Enqueue",command=enqueue).pack()
tk.Button(window,text="Dequeue",command=dequeue).pack()

queue_box = tk.Listbox(window,height=6,width=25)
queue_box.pack(pady=5)

# Linked List
tk.Label(window,text="Linked List",font=("Arial",14)).pack()
tk.Button(window,text="Insert Node",command=insert_node).pack()
tk.Button(window,text="Delete Node",command=delete_node).pack()

list_box = tk.Listbox(window,height=6,width=25)
list_box.pack(pady=5)

# History
tk.Label(window,text="Operation History",font=("Arial",14)).pack()

history_box = tk.Listbox(window,height=8,width=40)
history_box.pack(pady=5)

window.mainloop()