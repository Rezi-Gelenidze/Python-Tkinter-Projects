from tkinter import *

# legal chars
allowed_chars = "1234567890+-*/.()"

#root window
root = Tk()

root.geometry("180x310")
root.title("")
root.configure(bg='#1a1a2e')

def scan(input_text):
    for char in input_text:
        if char not in allowed_chars:
            return False
    return True

def add_character(char):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + char)

def calculate():
    expression = entry.get()
    entry.delete(0, END)
    if scan(expression):
        try:
            result = eval(expression)
        except:
            entry.insert(0, "Error")
        else:
            entry.insert(0, result)
    else:
        entry.insert(0, "Invalid characters")




#---defining widgets---
# input field
entry = Entry(root, width=21, bg='#132743', fg='white')

# remove button
button_delete = Button(root, text="<-", padx=11, pady=8, bg='#132743', fg='white', command=lambda : entry.delete(len(entry.get())-1))

# clear button
button_C = Button(root, text="c", padx=15, pady=15, bg='#132743', fg='white', command=lambda : entry.delete(0, END))

# parentheses ()
button_lpar = Button(root, text="(", padx=16, pady=15, bg='#132743', fg='white', command=lambda : add_character("("))
button_rpar = Button(root, text=")", padx=16, pady=15, bg='#132743', fg='white', command=lambda : add_character(")"))

# number buttons 0-9
button_7 = Button(root, text="7", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("7"))
button_8 = Button(root, text="8", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("8"))
button_9 = Button(root, text="9", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("9"))
button_4 = Button(root, text="4", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("4"))
button_5 = Button(root, text="5", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("5"))
button_6 = Button(root, text="6", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("6"))
button_1 = Button(root, text="1", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("1"))
button_2 = Button(root, text="2", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("2"))
button_3 = Button(root, text="3", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("3"))
button_0 = Button(root, text="0", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("0"))

# + = x /
button_add = Button(root, text="+", padx=13, pady=15, bg='#132743', fg='white', command=lambda : add_character("+"))
button_sub = Button(root, text="-", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("-"))
button_mul = Button(root, text="*", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("*"))
button_div = Button(root, text="/", padx=15, pady=15, bg='#132743', fg='white', command=lambda : add_character("/"))

# floating point
button_point = Button(root, text=".", padx=16, pady=15, bg='#132743', fg='white', command=lambda : add_character("."))

# calculate (=) button
button_equal = Button(root, text="=", padx=36, pady=15, bg='#132743', fg='white', command=calculate)



#---adding widgets---
# input field
entry.grid(row=0, column=0, columnspan=3, ipady = 8)

# parentheses
button_lpar.grid(row=1, column=0)
button_rpar.grid(row=1, column=1)

# clear button
button_C.grid(row=1, column=2)

# remove last button
button_delete.grid(row=0, column=3)

# number buttons
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_0.grid(row=5, column=1)

# + = * /
button_div.grid(row=1, column=3)
button_mul.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_add.grid(row=4, column=3)

# floating point
button_point.grid(row=5, column=0)

# calculate (=) button
button_equal.grid(row=5, column=2, columnspan=2)

# mainloop
root.mainloop()