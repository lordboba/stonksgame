from discord.ext import commands, tasks
import discord
import os
import asyncio
import datetime as dt
from dotenv import load_dotenv

load_dotenv(".env")
client = commands.Bot(command_prefix='$', activity=discord.Game(name="Playing $help"))
TOKEN = os.environ["TOKEN"]
client.run(TOKEN)