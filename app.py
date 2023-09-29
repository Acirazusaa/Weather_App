import requests
import tkinter as tk
from PIL import Image, ImageTk

API_KEY = 'd26ccbceeef01b9e6027427e1c759969'

def get_weather_data(city):
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(city):
    weather_data = get_weather_data(city)
    if weather_data and weather_data.get('cod') != '404':
        weather = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])
        result_label.config(
            text=f"The weather in {city} is: {weather}\nThe temperature is: {temp}ºF")
    else:
        result_label.config(text="No City Found")

def search_weather():
    city = city_entry.get()
    display_weather(city)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Set the window size to 800x600
root.geometry("960x540")

# Load and display a background image
bg_image = Image.open("C:\\Users\\magis\\OneDrive\\Pictures\\Weather_App_Bg_With_Icon.png")  # Replace with the path to your background image
bg_image = bg_image.resize((960, 540), Image.LANCZOS)  # Corrected attribute name
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and pack UI elements
city_label = tk.Label(root, text="Enter city:", font=("Arial", 16, "bold"))
city_label.grid(row=0, column=0, columnspan=2, pady=20)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.grid(row=1, column=0, columnspan=2, pady=10)

search_button = tk.Button(root, text="Search", command=search_weather)
search_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", wraplength=300, font=("Arial", 14))  
result_label.grid(row=3, column=0, columnspan=2, pady=100, padx=100)

root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
root.mainloop()
