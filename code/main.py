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
from start import st, create_game
from end import endG, shut_down
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext


# print("hi my name is bob")
load_dotenv()
client = commands.Bot(command_prefix='$', activity=discord.Game(name="Playing $help"))
slash = SlashCommand(client, sync_commands=True)
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

@client.command(name="start")
async def start(ctx,time:Optional[str]):
    await st(ctx, time)

@slash.component_callback()
async def yea(ctx: ComponentContext):
    await ctx.edit_origin(content="Game Started!", components=[])
    # print("Squid game")
    await create_game(ctx)

@slash.component_callback()
async def nou(ctx: ComponentContext):
    # await ctx.send()
    await ctx.edit_origin(content="Alright, looks like we're not starting a game here.",components=[])

@client.command(name="end")
async def end(ctx):
    await endG(ctx)

@slash.component_callback()
async def ye_end(ctx: ComponentContext):
    await ctx.edit_origin(content="Game Ended.", components=[])
    # print("Squid game")
    await shut_down(ctx)

@slash.component_callback()
async def no_cont(ctx: ComponentContext):
    # await ctx.send()
    await ctx.edit_origin(content="Alright, looks like we're not ending the game.",components=[])

TOKEN = os.environ["token"]
client.run(TOKEN)