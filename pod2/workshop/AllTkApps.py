import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import socket

# Function to create the Calculator widget
def create_calculator_widget(parent):
    def handle_button_click(button_text):
        current = entry.get()
        entry.delete(0, tk.END)  # Clear the entry
        entry.insert(0, current + button_text)  # Append button text

    def clear_entry():
        entry.delete(0, tk.END)  # Clear the entry

    def evaluate_expression():
        try:
            result = eval(entry.get())  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(0, str(result))  # Show the result
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")  # Handle evaluation errors

    # Create the calculator frame
    calc_frame = ttk.Frame(parent)

    # Create entry widget
    entry = ttk.Entry(calc_frame, width=16, font=('Arial', 24), justify='right')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Create buttons
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]

    row_val, col_val = 1, 0
    for button in buttons:
        if button == '=':
            btn = ttk.Button(calc_frame, text=button, command=evaluate_expression)
        elif button == 'C':
            btn = ttk.Button(calc_frame, text=button, command=clear_entry)
        else:
            btn = ttk.Button(calc_frame, text=button, command=lambda b=button: handle_button_click(b))

        btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Back button
    back_button = ttk.Button(calc_frame, text="Back", command=show_main_menu)
    back_button.grid(row=row_val, column=0, columnspan=4, pady=10)

    # Configure grid weights for proper expansion
    for i in range(4):
        calc_frame.grid_columnconfigure(i, weight=1)
    for i in range(1, 5):
        calc_frame.grid_rowconfigure(i, weight=1)

    return calc_frame

# Function to create the Weather widget
def create_weather_widget(parent):
    def fetch_weather_data(city):
        api_key = "4804edc641ffb40eaa99c7c33f2e0cb2"  # Replace with your API key
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

        try:
            socket.create_connection(("www.google.com", 80))  # Check internet connection
            response = requests.get(complete_url)
            data = response.json()

            if data['cod'] == 200:
                main = data['main']
                wind = data['wind']
                weather_description = data['weather'][0]['description']

                weather_info = (
                    f"Temperature: {main['temp']}°C\n"
                    f"Humidity: {main['humidity']}%\n"
                    f"Weather: {weather_description.capitalize()}\n"
                    f"Wind Speed: {wind['speed']} m/s"
                )
                return weather_info
            else:
                raise ValueError("City not found")

        except socket.gaierror:
            messagebox.showerror("Error", "No internet connection!")
            return None

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return None

        except Exception:
            messagebox.showerror("Error", "An unexpected error occurred!")
            return None

    def display_weather():
        city = city_entry.get()
        if city:
            weather = fetch_weather_data(city)
            if weather:
                weather_label.config(text=weather)
        else:
            messagebox.showwarning("Input Error", "Please enter a city name.")

    # Create the weather frame
    weather_frame = ttk.Frame(parent)

    # City Label and Entry
    city_label = ttk.Label(weather_frame, text="Enter City:", font=('Helvetica', 14, 'bold'))
    city_label.pack(pady=10)

    city_entry = ttk.Entry(weather_frame, width=25, font=('Helvetica', 12))
    city_entry.pack(pady=5)

    # Get Weather Button
    weather_button = ttk.Button(weather_frame, text="Get Weather", command=display_weather)
    weather_button.pack(pady=15)

    # Weather Info Label
    weather_label = ttk.Label(weather_frame, text="", font=('Helvetica', 12))
    weather_label.pack(pady=20)

    # Back button
    back_button = ttk.Button(weather_frame, text="Back", command=show_main_menu)
    back_button.pack(pady=10)

    return weather_frame

# Function to create the Menu Bar
def create_menu_bar_widget(parent):
    def new_file():
        note_section.delete(1.0, tk.END)  # Clear the note section

    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                note_section.delete(1.0, tk.END)  # Clear current notes
                note_section.insert(tk.END, file.read())  # Insert file contents

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_path:
            with open(file_path, 'w') as file:
                file.write(note_section.get(1.0, tk.END))  # Save current notes

    def exit_application():
        parent.quit()

    # Create the menu frame
    menu_frame = ttk.Frame(parent)

    # Create Menubutton and dropdown menu
    menubutton = tk.Menubutton(menu_frame, text="File", relief=tk.RAISED)
    menu = tk.Menu(menubutton, tearoff=0)
    menubutton.config(menu=menu)

    # Add menu options
    menu.add_command(label='New', command=new_file)
    menu.add_command(label='Open', command=open_file)
    menu.add_command(label='Save', command=save_file)
    menu.add_separator()
    menu.add_command(label='Exit', command=exit_application)

    # Display the Menubutton in the frame
    menubutton.pack(side='left')

    # Create a Text widget for notes
    global note_section
    note_section = tk.Text(menu_frame, wrap='word')
    note_section.pack(expand=True, fill='both')

    # Back button
    back_button = ttk.Button(menu_frame, text="Back", command=show_main_menu)
    back_button.pack(pady=10)

    return menu_frame

# Function to show the main menu
def show_main_menu():
    for widget in main_frame.winfo_children():
        widget.pack_forget()
    main_menu_frame.pack(fill='both', expand=True)

# Function to show the Calculator
def show_calculator():
    for widget in main_frame.winfo_children():
        widget.pack_forget()
    calc_frame.pack(fill='both', expand=True)

# Function to show the Weather Widget
def show_weather():
    for widget in main_frame.winfo_children():
        widget.pack_forget()
    weather_frame.pack(fill='both', expand=True)

# Function to show the Menu Bar
def show_menu_bar():
    for widget in main_frame.winfo_children():
        widget.pack_forget()
    menu_frame.pack(fill='both', expand=True)

# Main application setup
root = tk.Tk()
root.title("Widgets in One Window")
root.geometry("400x400")

# Create main frames
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Main Menu
main_menu_frame = ttk.Frame(main_frame)
ttk.Label(main_menu_frame, text="Choose a Widget:", font=('Helvetica', 16)).pack(pady=20)

calculator_button = ttk.Button(main_menu_frame, text="Calculator", command=show_calculator)
calculator_button.pack(pady=5)

weather_button = ttk.Button(main_menu_frame, text="Weather", command=show_weather)
weather_button.pack(pady=5)

menu_button = ttk.Button(main_menu_frame, text="Menu Bar", command=show_menu_bar)
menu_button.pack(pady=5)

# Create frames for each widget
calc_frame = create_calculator_widget(main_frame)
weather_frame = create_weather_widget(main_frame)
menu_frame = create_menu_bar_widget(main_frame)

# Show the main menu initially
show_main_menu()

# Start the Tkinter main loop
root.mainloop()
