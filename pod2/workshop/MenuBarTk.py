import tkinter as tk
from tkinter import Menu, filedialog

# Create the main window
window = tk.Tk()
window.title("Menu Bar Example")
window.geometry("400x300")

# Function to handle the 'New' action 
def new_file():
    note_section.delete(1.0, tk.END)  # Clear the note section

# Function to handle 'Open' action 
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
        filetypes=[("Text files", "*.txt"),
        ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            note_section.delete(1.0, tk.END)  # Clear current notes
            note_section.insert(tk.END, file.read())  # Insert the file contents

# Function to handle 'Save' action 
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
    filetypes=[("Text files", "*.txt"),
    ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'w') as file:
            file.write(note_section.get(1.0, tk.END))  # Save current notes

# Function to handle the 'Exit' action 
def exit_app():
    window.quit()

# Create a Frame to hold the menu
menu_frame = tk.Frame(window)
menu_frame.pack(fill='x')

# Create Menubutton and dropdown menu
menubutton = tk.Menubutton(menu_frame, text="File", relief=tk.RAISED)
menu = Menu(menubutton, tearoff=0)
menubutton.config(menu=menu)

# Add menu options
menu.add_command(label='New', command=new_file)
menu.add_command(label='Open', command=open_file)
menu.add_command(label='Save', command=save_file)
menu.add_separator()
menu.add_command(label='Exit', command=exit_app)

# Display the Menubutton in the frame
menubutton.pack(side='left')

# Create a Text widget for notes
note_section = tk.Text(window, wrap='word')
note_section.pack(expand=True, fill='both')

# Start the Tkinter main loop
window.mainloop()