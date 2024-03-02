from random import randint
from typing import Final
import os 
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN')

intentes:discord.Intents=discord.Intents.default()
intentes.messages=True
intentes.reactions=True
intentes.presences=True
intentes.typing=True

client:discord.Client=discord.Client(intents=intentes)


    
def main()->None:
    client.run(TOKEN)
    
    
    
    
if __name__=="__main__":
  
  main()