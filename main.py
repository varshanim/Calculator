import tkinter as tk
cal = ""

def add_to_calculation(symbol):
    global cal
    cal += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, cal)

def evaluate_calculation():
    global cal
    try:
        cal = str(eval(cal))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, cal)
        cal = ""
    except:
        clear_field()
        text_result.insert(1.0, " Error")

def clear_field():
    global cal
    cal = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("Varsha's Calculator")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=19, font=("Sans Serif", 25))
text_result.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=4, font=("Sans Serif", 14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=4, font=("Sans Serif", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=4, font=("Sans Serif", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=4, font=("Sans Serif", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=4, font=("Sans Serif", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=4, font=("Sans Serif", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=4, font=("Sans Serif", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=4, font=("Sans Serif", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=4, font=("Sans Serif", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=4, font=("Sans Serif", 14))
btn0.grid(row=5, column=2)
btnopen = tk.Button(root, text="(", command=lambda:add_to_calculation("("), width=4, font=("Sans Serif", 14))
btnopen.grid(row=5, column=1)
btnclose = tk.Button(root, text=")", command=lambda:add_to_calculation(")"), width=4, font=("Sans Serif", 14))
btnclose.grid(row=5, column=3)
btnplus = tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=4, font=("Sans Serif", 14))
btnplus.grid(row=2, column=4)
btnminus = tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=4, font=("Sans Serif", 14))
btnminus.grid(row=3, column=4)
btnmul = tk.Button(root, text="*", command=lambda:add_to_calculation("*"), width=4, font=("Sans Serif", 14))
btnmul.grid(row=4, column=4)
btndiv = tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=4, font=("Sans Serif", 14))
btndiv.grid(row=5, column=4)
btnequals = tk.Button(root, text="=", command=evaluate_calculation, width=13, font=("Sans Serif", 14))
btnequals.grid(row=6, column=3, columnspan=2)
btnclear = tk.Button(root, text="AC", command=clear_field, width=13, font=("Sans Serif", 14))
btnclear.grid(row=6, column=1, columnspan=2)
root.mainloop()