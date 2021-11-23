#
import os
import asyncio
import datetime as dt
import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
# print("hi my name is bob")
load_dotenv()
client = commands.Bot(command_prefix='$', activity=discord.Game(name="Playing $help"))
# print(os.environ['VIRTUAL_ENV'])
# print(os.environ.get("token"))
TOKEN = os.environ["token"]
client.run(TOKEN)