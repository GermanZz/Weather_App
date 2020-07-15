from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import time
import requests
from api_key import KEY #Delete this, there is my API key


def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning(title='Warning', message='Please enter in format City, Country_code !')
    else:
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric'
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label['text'] = print_weather(weather)


def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        hum = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
        sunset = time.strftime('%H:%M:%S', sunset_struct_time)
        return f'Location: {city}, {country}\nTemperature: {temp} °С\nHumidity: {hum}\n' \
               f'Pressure: {press} mmHg\nWind speed: {wind} m/s\n' \
               f'Weather conditions: {desc.title()}\nSunrise: {sunrise}\nSunset: {sunset}'
    except:
        return 'Wrong data was entered !'


API_KEY = KEY # Your API key here
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

root = ThemedTk(theme='arc')
root.title('Weather Now')
# root.iconbitmap('favicon.ico')
root.geometry('500x400+500+200')
root.resizable(False, False)

s = ttk.Style()
s.configure('TLabel', padding=10, font='Consolas 18')

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)
entry.bind('<Return>', get_weather)

button = ttk.Button(top_frame, text='SHOW WEATHER', command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

low_frame = ttk.Frame(root)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(low_frame, anchor='nw')
label.place(relwidth=1, relheight=1)

root.mainloop()
