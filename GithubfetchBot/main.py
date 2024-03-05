
from random import randint
from typing import Final
import os 
import discord
from dotenv import load_dotenv
from discord.ext import commands
import settings

load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN')
    
intentes:discord.Intents=discord.Intents.all()

client:discord.Client=discord.Client(intents=intentes)

logger=settings.logging.getLogger("bot")
intents=discord.Intents.default()
bot=commands.Bot(command_prefix='!',intents=intents)


def run_bot()->None:
  
  
  @bot.event
  async def on_ready():
    logger.info(f'user:{bot.user.name}  (ID:{bot.user.id}) has connected to Discord!')
  
  @bot.command(
    help="Responds with 'Pong!' and the latency in milliseconds."
  )
  async def ding(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms')
    
  bot.run(TOKEN,root_logger=True)
    
    
    
    
if __name__=="__main__":
  run_bot()

# কোডিং চাঙ্গে আমি ভাষী গাঙে 