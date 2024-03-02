import os
import discord
import requests 
from typing import Final
from dotenv import load_dotenv
import pprint

load_dotenv()
API_KEY:Final[str]=os.getenv('API_KEY')
cityname:Final[str]="Dhaka"
url=f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}"

data=requests.get(url).json()

message:str=f"City: {data['name']}\nTemperature: {round(data['main']['temp']-273.15,2)} °C\nHumidity: {data['main']['humidity']}%\nDescription: {data['weather'][0]['description']}"


