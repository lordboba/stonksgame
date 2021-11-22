from discord.ext import commands, tasks
import discord
import os
import asyncio
import datetime as dt
client = commands.Bot(command_prefix='$', activity=discord.Game(name="Playing $help"))
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
client.run(DISCORD_TOKEN)