from tkinter import *
from tkinter import ttk

expression = ""
commands = ['AC', "+/-", "%", "/", "7", "8", "9", "x",
            "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="]
root = Tk()
root["bg"] = "#1C1C1C"
root.geometry("450x380")
frame1 = Frame(root, bg="#1C1C1C", pady=20)
frame1.pack()
frame2 = Frame(root, bg="#1C1C1C", pady=20)
frame2.pack()
custom_font = ("Helvetica", 12, "bold")

text_input = Text(frame1, width=40, height=1, spacing1=20, spacing3=20, font=custom_font, foreground="#fff",
                  background='#505050')
text_input.xview_moveto(1)
text_input.pack()
# Create buttons and place them in a 4x5 grid
for i in range(4):
    for j in range(4):
        index = i * 4 + j
        button_text = f"Button {i*5 + j + 1}"
        bcolor = '#505050'
        if (j == 3):
            bcolor = '#FF9500'
        Button(frame2, text=commands[index], width=10, font=custom_font, foreground="#fff",
               height=2, background=bcolor, command=lambda cmd=commands[i*4 + j]: operation(cmd)).grid(row=i, column=j)

Button(frame2, text=commands[16], width=21, height=2,  font=custom_font, foreground="#fff",
       background='#505050', command=lambda cmd=commands[16]: operation(cmd)).grid(row=4, column=0, columnspan=2)
Button(frame2, text=commands[17], width=10, height=2,  font=custom_font, foreground="#fff",
       background='#505050', command=lambda cmd=commands[17]: operation(cmd)).grid(row=4, column=2)
Button(frame2, text=commands[18], width=10, height=2,  font=custom_font, foreground="#fff",
       background='#FF9500', command=lambda cmd=commands[18]: operation(cmd)).grid(row=4, column=3)


def operation(cmd):
    global expression
    if cmd == "AC":
        expression = ""
    elif cmd == "=":
        expression = expression.replace("x", "*")
        expression = str(eval(expression))
    elif cmd == "+/-":
        if (expression[0] == "-"):
            expression = expression[1:]
        else:
            expression = "-" + expression
    else:
        expression = expression + cmd
    text_input.delete("1.0", "end")
    text_input.insert("1.0", expression)


root.mainloop()
