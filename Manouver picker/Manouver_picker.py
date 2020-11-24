import tkinter as tk
from tkinter import ttk
import random

LIST = []
PICKED = []


def add_manouver():
    global LIST
    list_show.insert(tk.END, content.get())
    LIST.append(content.get())
    user_input.delete(0, tk.END)
    user_input.focus_set()

def delete_manouver():
    global LIST
    selected = list_show.get(list_show.curselection())
    list_show.delete(tk.ANCHOR)
    index = LIST[LIST.index(selected)]
    LIST.pop(LIST.index(selected))


def pick_manouver():
    global LIST, PICKED
    if len(PICKED) <= num_active.get()-1:
        pick = LIST.pop(random.randint(0, len(LIST)-1))
        PICKED.append(pick)
        list_show.delete(list_show.get(0, tk.END).index(pick))
        pick_show.insert(tk.END, pick)
        user_input.focus_set()
    else:
        pass

def delete_sel_manouver():
    global PICKED
    selected = pick_show.get(pick_show.curselection())
    pick_show.delete(tk.ANCHOR)
    index = PICKED.index(selected)
    PICKED.pop(PICKED.index(selected))

root = tk.Tk()
root.title('Manouver picker')
root.columnconfigure(0, weight = 1)

main = ttk.Frame(root, padding = (30, 15))
main.grid()

top_text = ttk.Label(main, text = 'Manouver Picker!', anchor = 'center')
top_text.grid(column=0, row=0, columnspan=3, sticky='EW')

content = tk.StringVar()
user_input = tk.Entry(main, textvariable = content)
user_input.grid(column=0, row=1, sticky='EW', pady=10)
user_input.focus_set()

add_button = ttk.Button(main, text='Add manouver', command=add_manouver)
add_button.grid(column=1, row=1)

del_button = ttk.Button(main, text = 'Delete manouver', command = delete_manouver)
del_button.grid(column=2, row=1)

list_show = tk.Listbox(main, height = 8, width = 40)
list_show.grid(column=0,row=2, columnspan=3, pady=10, sticky='EW')

number_label = ttk.Label(main, text = 'Number of active manouvers: ')
number_label.grid(column=0, row=3, columnspan=2, sticky='EW')

num_active = tk.IntVar()
number_input = tk.Entry(main, textvariable = num_active)
number_input.grid(column=2, row=3, pady=10)

pick_button = ttk.Button(main, text = 'Pick manouvers', command = pick_manouver)
pick_button.grid(column=0, row=4, columnspan=3, sticky='EW', pady=10)

pick_show = tk.Listbox(main, height = num_active.get(), width = 40)
pick_show.grid(column=0, row=5, columnspan=3, sticky='EW', pady=10)

del_sel_button = ttk.Button(main, text = 'Delete picked manouver', command = delete_sel_manouver)
del_sel_button.grid(column=0, row=6, columnspan=3, pady=10)

tk.mainloop()

list = []
picked = []
