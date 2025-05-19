import requests
import customtkinter as ctk

API_KEY = "9adb01131fed4cf115c54743bde367f8"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pl"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        feels = data['main']['feels_like']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        clouds = data['clouds']['all']
        return (
            f"Pogoda w {city}\n"
            f"{'Opis:':<16}{weather_description.capitalize()}\n"
            f"{'Temperatura:':<16}🌡️ {temperature}°C\n"
            f"{'Odczuwalna:':<16}{feels}°C\n"
            f"{'Zachmurzenie:':<16}☁️ {clouds}%\n"
            f"{'Wilgotność:':<16}💧 {humidity}%\n"
            f"{'Wiatr:':<16}🌪️ {wind_speed} m/s\n"
            f"{'Ciśnienie:':<16}{pressure} hPa\n"
        )
    else:
        return f"Nie można pobrać danych o pogodzie dla miasta {city}. Sprawdź nazwę miasta lub spróbuj ponownie później."

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        weather_label.configure(text=weather_info)
    else:
        weather_label.configure(text="Proszę wpisać nazwę miasta.")

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("Pogodynka")
root.geometry("400x450")

frame = ctk.CTkFrame(root, corner_radius=5)
frame.pack(fill="both", expand=True)

welcome_label = ctk.CTkLabel(frame, text="🌦️Pogodynka", font=("Segoe UI", 22, "bold"))
welcome_label.pack(pady=(20, 5))

subtitle = ctk.CTkLabel(frame, text="Wpisz nazwę miasta:", font=("Segoe UI", 13))
subtitle.pack(pady=(0, 10))

city_entry = ctk.CTkEntry(frame, font=("Segoe UI", 13), placeholder_text="Np. Wrocław")
city_entry.pack(pady=(0, 14), padx=16, fill='x')

submit_button = ctk.CTkButton(frame, text="Sprawdź pogodę", font=("Segoe UI", 13, "bold"), command=show_weather)
submit_button.pack(pady=(0, 18))

weather_label = ctk.CTkLabel(frame, text="", font=("Segoe UI", 20), justify="left", anchor="center")
weather_label.pack(pady=8, padx=12, fill="both")

root.mainloop()
