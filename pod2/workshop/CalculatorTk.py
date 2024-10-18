import tkinter as tk
from tkinter import ttk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry
    entry.insert(0, current + button_text)  # Append the clicked button's text

def clear():
    entry.delete(0, tk.END)  # Clear the entry

def evaluate():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))  # Show the result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")  # Handle any evaluation errors

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget
entry = ttk.Entry(root, width=16, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = ttk.Button(root, text=button, command=evaluate)
    elif button == 'C':
        btn = ttk.Button(root, text=button, command=clear)
    else:
        btn = ttk.Button(root, text=button, command=lambda b=button: click(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights for proper expansion
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
