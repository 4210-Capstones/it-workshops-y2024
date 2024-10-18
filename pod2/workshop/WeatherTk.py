import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import requests
import socket

# Function to get weather data
def get_weather(city):
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

            temp = main['temp']
            humidity = main['humidity']
            wind_speed = wind['speed']

            weather_data = (f"Temperature: {temp}Â°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Weather: {weather_description.capitalize()}\n"
                            f"Wind Speed: {wind_speed} m/s")

            return weather_data

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

# Function to display weather
def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        if weather:
            weather_label.config(text=weather)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Create the main window
root = tk.Tk()
root.title("Weather Widget")
root.geometry("350x300")

# City Label and Entry
city_label = ttk.Label(root, text="Enter City:", font=('Helvetica', 14, 'bold'))
city_label.pack(pady=10)

city_entry = ttk.Entry(root, width=25, font=('Helvetica', 12))
city_entry.pack(pady=5)

# Get Weather Button
weather_button = ttk.Button(root, text="Get Weather", command=show_weather)
weather_button.pack(pady=15)

# Weather Info Label
weather_label = ttk.Label(root, text="", font=('Helvetica', 12))
weather_label.pack(pady=20)

# Run the application
root.mainloop()