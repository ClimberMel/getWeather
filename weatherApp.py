# weatherApp.py
# Created:  2021-12-04
# Author:   Mel
# 
# This version works and will write the forecast to a file to be saved
# Other versions starting with gui work at taking this and making a GUI app out of it


# import the weather module
import python_weather
import asyncio
from datetime import datetime

# for the GUI
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

async def getweather():
    # some basic variables
    today = datetime.today().strftime('%Y-%m-%d')
    loc = "Port Moody BC"
    
    
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find(loc)

    # returns the current day's forecast temperature (int)
    #print('The current temperature today ' + today + ' in ' + loc + ' is: ' + str(weather.current.temperature))
    currWeather = str(weather.current.temperature)

    # get the weather forecast for a few days
    #print('The 5 day forecast for ' + loc + ' is: ')
    fcast = []
    f = {}
    for forecast in weather.forecasts:
        date_time = forecast.date
        date_time_str = date_time.date()
        #print(date_time_str, forecast.sky_text, 'High: ' + str(forecast.high), 'Low: ' + str(forecast.low))
        f = (date_time_str, forecast.sky_text, forecast.high, forecast.low)
        #print(f)
        fcast.append(f)
    #print(fcast)
    outP = 'Z:/VSCode-projects/myOutput/weather/' + str(today) + '_weatherPM.txt'
    
    fcdf = pd.DataFrame(fcast)
    fcdf.columns =['Date', 'Sky', 'High', 'Low']
    df2 = fcdf.to_string(index=False)
    print(df2)
    
    with open(outP, 'w') as wOut:
        print(df2, file=wOut)
    


    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
    #print(loop.fcast)