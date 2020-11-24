import random
import tkinter as tk
from tkinter import ttk


def get_mod(attribute):
    mod = 0
    if attribute == 1:
        mod = '-5'
    elif attribute == 2 or attribute == 3:
        mod = '-4'
    elif attribute == 4 or attribute == 5:
        mod = '-3'
    elif attribute == 6 or attribute ==7:
        mod = '-2'
    elif attribute == 8 or attribute == 9:
        mod = '-1'
    elif attribute == 10 or attribute == 11:
        mod = '0'
    elif attribute == 12 or attribute == 13:
        mod = '+1'
    elif attribute == 14 or attribute == 15:
        mod = '+2'
    elif attribute == 16 or attribute == 17:
        mod = '+3'
    elif attribute == 18 or attribute == 19:
        mod = '+4'
    elif  attribute == 20 or attribute == 21:
        mod = '+5'
    return mod

def get_attr():
    attributes = []
    rolls_all = []

    for x in range(7):
        rolls = []
        for y in range(4):
            rolls.append(random.randint(1,6))
        rolls.sort(reverse=True)
        print(rolls)
        x = rolls.copy()
        rolls_all.append(x)
        print(rolls)
        print(rolls_all)
        rolls.pop(-1)
        attributes.append(sum(rolls))

    attributes.sort(reverse=True)
    attributes.pop(-1)
    return attributes, rolls_all

def roll_attr(get_attr, get_mod,*args):
    global atr_label, second_frame
    second_frame.destroy()
    second_frame = ttk.Frame(root)
    second_frame.grid(row=1, pady=10)
    generated_attr = get_attr()

    for attribute in generated_attr[0]:
        mod = get_mod(attribute)
        atr_label = ttk.Label(
            second_frame,
            text = f'Attribute: {attribute}  mod: {mod}',
            anchor = 'center')
        atr_label.grid(column = 0, sticky='EW')

    txt_label = ttk.Label(main, text = "Your rolls: ")
    txt_label.grid(column = 0, row=2, pady=10)

    roll_box = tk.Text(main, height=8, width = 22)
    roll_box.grid(column=0, row=3, pady=5)

    generated_attr[1].sort()
    for roll in generated_attr[1]:
        roll_box.insert(tk.END,roll)
        roll_box.insert(tk.END,f'     ATTR: {sum(roll) - roll[-1]}')
        roll_box.insert(tk.END,'\n')




root = tk.Tk()
root.title('Attributes generator')
root.columnconfigure(0, weight = 1)

main = ttk.Frame(root)
main.grid(padx = 30, pady=10)
second_frame = ttk.Frame(root)
second_frame.grid(row=1)

atr_show = ttk.Label(main, text='Attribute generator', anchor = 'center')
atr_show.grid(column=0, row=0, columnspan = 2, sticky='EW', padx=10, pady=10)

atr_button = ttk.Button(main, text='Generate')
atr_button.config(command = lambda: atr_label.config(text=roll_attr(get_attr, get_mod)))
atr_button.grid(column=0, row=1, sticky='EW', padx=10, pady=10)

atr_label = ttk.Label(second_frame, text = 'Empty')

root.mainloop()
