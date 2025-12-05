import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x520")
root.config(bg="blue")

expression = ""

# ================= DISPLAY ==================
display = tk.Entry(root, font=("Calibri", 24), width=15, bg="black", fg="lime", border=5, justify="right")
display.pack(pady=15)

def btn_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def equal():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


# ================ SCIENTIFIC FUNCTIONS ===============
def scientific_action(func):
    global expression
    try:
        value = float(display.get())
        if func == "sin": result = math.sin(math.radians(value))
        elif func == "cos": result = math.cos(math.radians(value))
        elif func == "tan": result = math.tan(math.radians(value))
        elif func == "log": result = math.log10(value)
        elif func == "sqrt": result = math.sqrt(value)
        elif func == "fact": result = math.factorial(int(value))
        elif func == "π": result = math.pi
        elif func == "e": result = math.e

        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = str(result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# ============== BUTTON AREA ==============
button_frame = tk.Frame(root, bg="#222")
button_frame.pack()

scientific_mode = False

def update_buttons():
    for widget in button_frame.winfo_children():
        widget.destroy()

    # ----- First row: Arithmetic always visible -----
    top_row = tk.Frame(button_frame, bg="#222")
    top_row.pack(pady=5)

    operations = ["/", "*", "-", "+"]

    for op in operations:
        tk.Button(top_row, text=op, width=5, height=2, bg="#ff9800", fg="black",
                  command=lambda o=op: btn_click(o), font=("Calibri", 16)).pack(side="left", padx=4)

    # ----- Number Mode -----
    if not scientific_mode:
        numbers = [
            ("7", "8", "9"),
            ("4", "5", "6"),
            ("1", "2", "3"),
            ("0", ".", "="),
        ]
        for row in numbers:
            row_frame = tk.Frame(button_frame, bg="#222")
            row_frame.pack(pady=5)
            for item in row:
                if item == "=":
                    tk.Button(row_frame, text=item, width=5, height=2, bg="orange", fg="black",
                              command=equal, font=("Calibri", 16)).pack(side="left", padx=5)
                else:
                    tk.Button(row_frame, text=item, width=5, height=2, bg="#333", fg="white",
                              command=lambda v=item: btn_click(v), font=("Calibri", 16)).pack(side="left", padx=5)

    # ----- Scientific Mode Buttons (replace numbers) -----
    else:
        functions = [
            ("sin", "cos", "tan"),
            ("log", "sqrt", "fact"),
            ("π", "e", "^")
        ]
        for row in functions:
            sci_row = tk.Frame(button_frame, bg="#222")
            sci_row.pack(pady=5)
            for item in row:
                if item == "^":
                    tk.Button(sci_row, text=item, width=5, height=2, bg="#607d8b", fg="white",
                              command=lambda: btn_click("**"), font=("Calibri", 16)).pack(side="left", padx=5)
                else:
                    tk.Button(sci_row, text=item, width=5, height=2, bg="#455a64", fg="white",
                              command=lambda f=item: scientific_action(f), font=("Calibri", 16)).pack(side="left", padx=5)


# Load UI first time
update_buttons()

# -------- BOTTOM CONTROLS --------
control_frame = tk.Frame(root, bg="#222")
control_frame.pack(pady=15)

def toggle_mode():
    global scientific_mode
    scientific_mode = not scientific_mode
    toggle_btn.config(text="Normal Mode" if scientific_mode else "Scientific Mode")
    update_buttons()

tk.Button(control_frame, text="C", width=14, height=2, bg="red", fg="white",
         command=clear, font=("Calibri", 16)).grid(row=0, column=0, padx=10)

toggle_btn = tk.Button(control_frame, text="Scientific Mode", width=14, height=2, bg="green", fg="white",
                       command=toggle_mode, font=("Calibri", 16))
toggle_btn.grid(row=0, column=1)

root.mainloop()
