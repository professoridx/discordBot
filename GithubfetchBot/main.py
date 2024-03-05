
from random import randint
from typing import Final
import os 
import discord
from dotenv import load_dotenv
from discord.ext import commands
import log 
import logging
logging=log.logging.getLogger("bot")

load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN')

def run_bot()->None:
  intents:discord.Intents=discord.Intents.default()
  bot=commands.Bot(command_prefix='!',intents=intents)
  
  @bot.event
  async def on_ready():
    log.info(f'{bot.user.name}  (ID:{bot.user.id}) has connected to Discord!')
    
    bot.run(TOKEN,root_logger=True)
    
    
    
intentes:discord.Intents=discord.Intents.default()
# intentes.messages=True
# intentes.reactions=True
# intentes.presences=True
# intentes.typing=True

client:discord.Client=discord.Client(intents=intentes)


    
def main()->None:
    client.run(TOKEN)
    
    
    
    
if __name__=="__main__":
  
  main()