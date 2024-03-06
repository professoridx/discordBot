
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
