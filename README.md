# Irrigation
Irrigation is a python app based on [Ben Finio's instructable](https://www.instructables.com/Raspberry-Pi-Controlled-Irrigation-System/).

So far the application is in french.
The app is built with tkinter and can be used to control the GPIOs easily.

![2022-08-16-223432_800x480_scrot](https://user-images.githubusercontent.com/55147670/184980392-277c1214-ec67-43a9-bcb7-f38063fb8678.png)

- "Arroser" activates GPIO number 17 to trigger the irrigation. 
- "Stop" puts the input of GPIO number 17 to GPIO.low.
- "Arrosage 5 minutes" let's GPIO number 17 run for 5 minutes.

The app also uses a connection to picam2 to show the input of a camera if one is plugged.

The app also uses [AskPython's code](https://www.askpython.com/python/examples/gui-weather-app-in-python) to show the current weather condition using Open Weather Map.
