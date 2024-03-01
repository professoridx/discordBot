from typing import Final
import os 
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN')

