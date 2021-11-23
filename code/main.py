#
import os
import asyncio
import datetime as dt
import discord
from discord.ext import commands, tasks
from invite import invited
from feedback import dev_fb
from help import halp
from dotenv import load_dotenv
from typing import Optional
# print("hi my name is bob")
load_dotenv()
client = commands.Bot(command_prefix='$', activity=discord.Game(name="Playing $help"))
# print(os.environ['VIRTUAL_ENV'])
# print(os.environ.get("token"))
client.remove_command("help")

@client.command(name="invite")
async def invite(ctx):
    await invited(ctx)

@client.command(name="inv")
async def inv(ctx):
    await invited(ctx)

@client.command(name="feedback")
async def feedback(ctx):
    await dev_fb(ctx,client)

@client.command(name="fb")
async def fb(ctx):
    await dev_fb(ctx,client)

@client.command(name="help")
async def help(ctx,set1:Optional[str], set2:Optional[str]):
    await halp(ctx, set1,set2)

TOKEN = os.environ["token"]
client.run(TOKEN)