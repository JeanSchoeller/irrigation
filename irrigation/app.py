#! /usr/bin/python
from tkinter import *
import RPi.GPIO as GPIO
from time import strftime as strf
import requests
import json
from picamera2 import Picamera2, Preview
import time as t
from datetime import datetime, time, timezone, date
#Import RPI GPIOS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup((17,22), GPIO.OUT)
log_file = "irrigation.txt"
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def open_valve():
    GPIO.output(17,GPIO.HIGH)
    f= open(log_file, "a")
    f.write("Valve ouverte à: %s (ouverture via app) \n" % datetime.now())
    f.close()
def close_valve():
    GPIO.output(17, GPIO.LOW)
    f= open(log_file, "a")
    f.write("Valve fermée à: %s (fermeture via app) \n" % datetime.now())
    f.close()
def open_valve_five():
    GPIO.output(17, GPIO.HIGH)
    t.sleep(300)
    GPIO.output(17, GPIO.LOW)
    f= open(log_file, "a")
    f.write("Arrosage 5 minutes: %s \n" % datetime.now())
    f.close()
#Tk code:

def camera_preview():
    picam2 = Picamera2()
    picam2.start_preview(Preview.QTGL)
    preview_config = picam2.preview_configuration()
    picam2.configure(preview_config)
    picam2.start()
    t.sleep(10)
    picam2.stop()
    picam2.stop_preview()
class App(Frame):
    def __init__(self, master= None):
        Frame.__init__(self,master)
        self.master = master
        self.label_weather = Label(text="")
        self.label_weather.place(x=10,y=200)
        self.showWeather
        self.label = Label(text="")
        self.label.place(x=710, y = 50)
        self.label_horloge = Label(text="Horloge",font = ("Arial Bold", 14))
        self.label_horloge.place(x=705, y=10)
        self.update_clock
        self.label_potager = Label(text = "Arrosage potager", font =("Arial Bold", 22))
        self.label_potager.place(x=220, y=10)
        self.button_quit = Button(text = "Quitter", fg = "red", command = self.quit)
        self.button_quit.place(x=700,y=380)
        self.button_arrosage_on = Button(text = "Arroser", fg="blue",height = 5, width = 8, command = open_valve)
        self.button_arrosage_on.place(x=210, y=50)
        self.button_arrosage_off= Button(text = "Stop", fg="red",height = 5, width = 8, command = close_valve)
        self.button_arrosage_off.place(x=310, y=50)
        self.button_arrosage_five= Button(text = "Arrosage\n 5 minutes", fg="green",height = 5, width = 8, command = open_valve_five)
        self.button_arrosage_five.place(x=410, y=50)
        self.button_camera = Button(text="Camera", height =5, width = 8, command = camera_preview)
        self.button_camera.place(x=700, y =250)
    def showWeather(self):
        print("start") 
        city_name= "Menaggio"
        weather_url = "https://api.openweathermap.org/data/2.5/weather?q=menaggio&appid=31ceae673776cf2e67748b7fe00057e1" 
        response = requests.get(weather_url)
        weather_info = response.json()
        print("setup") 
        if weather_info['cod'] == 200:
            temp = int(weather_info['main']['temp']-273)
            feels_like_temp = int(weather_info['main']['feels_like']-273)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
 
            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)

                 
            weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
        else:
            weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
        self.label_weather.configure(text=weather)
        self.after(600000,self.showWeather)
    def update_clock(self):
        now= strf("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)
    def lines(self):
        canvas = Canvas(self, width ="800", height = "480")
        canvas.create_line(200,0,200,250)
        canvas.pack()

root = Tk()
app = App(root)
root.geometry("800x480")
root.title("Arrosage Menaggio")
root.after(1000, app.update_clock)
root.after(1000, app.showWeather)
root.mainloop()
