import tkinter as tk
import math

def click(event):
    global expression
    text = event.widget.cget("text")

    try:
        if text == "=":
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)

        elif text == "C":
            expression = ""
            entry_var.set("")

        elif text == "√":
            result = math.sqrt(float(expression))
            entry_var.set(result)
            expression = str(result)

        elif text == "sin":
            result = math.sin(math.radians(float(expression)))
            entry_var.set(result)
            expression = str(result)

        elif text == "cos":
            result = math.cos(math.radians(float(expression)))
            entry_var.set(result)
            expression = str(result)

        elif text == "tan":
            result = math.tan(math.radians(float(expression)))
            entry_var.set(result)
            expression = str(result)

        elif text == "log":
            result = math.log10(float(expression))
            entry_var.set(result)
            expression = str(result)

        elif text == "ln":
            result = math.log(float(expression))
            entry_var.set(result)
            expression = str(result)

        else:
            expression += text
            entry_var.set(expression)

    except:
        entry_var.set("Error")
        expression = ""

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x520")
root.configure(bg="#ffc0cb")   # Baby pink background 🎀

expression = ""
entry_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvar=entry_var,
    font="Arial 20",
    bd=10,
    relief=tk.RIDGE,
    bg="white",
    fg="#b03060"
)
entry.pack(fill="both", ipadx=8, pady=15)

buttons = [
    "7","8","9","/","sin",
    "4","5","6","*","cos",
    "1","2","3","-","tan",
    "0",".","+","=","C",
    "√","log","ln","(",")"
]

frame = tk.Frame(root, bg="#ffc0cb")
frame.pack()

row = 0
col = 0

for button in buttons:
    
    # Special button colors
    if button == "=":
        bg_color = "#ff69b4"   # Hot pink
    elif button == "C":
        bg_color = "#ff85a2"
    else:
        bg_color = "#ffb6c1"   # Soft pink

    b = tk.Button(
        frame,
        text=button,
        font="Arial 15",
        width=5,
        height=2,
        bg=bg_color,
        fg="white",
        activebackground="#ff1493",
        activeforeground="white",
        relief=tk.RAISED
    )

    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)

    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()