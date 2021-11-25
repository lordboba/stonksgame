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
from start import st, create_game, no_st
from end import endG, shut_down
from join import joined, add_user
from assets import items
from buy import afford, addAsset, remBuy
from market import markP
from sell import sold, sellEm, remS
from game import playing
from leaderboard import winnin
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
    await no_st(ctx)

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

@client.command(name="join")
async def join(ctx):
    await joined(ctx)

@slash.component_callback()
async def yejoin(ctx: ComponentContext):
    await ctx.edit_origin(content="Game successfully joined!.", components=[])
    # print("Squid game")
    await add_user(ctx)

@slash.component_callback()
async def nojoin(ctx: ComponentContext):
    # await ctx.send()
    await ctx.edit_origin(content="Looks like we're not joining this time.",components=[])

@client.command(name="assets")
async def assets(ctx):
    await items(ctx)

@client.command(name="buy")
async def buy(ctx, Stock:Optional[str], Quantity:Optional[str]):
    await afford(ctx,  os.environ["key"],Stock, Quantity)

@client.command(name="b")
async def b(ctx, Stock:Optional[str], Quantity:Optional[str]):
    await afford(ctx,  os.environ["key"],Stock, Quantity)

@slash.component_callback()
async def yebuy(ctx: ComponentContext):
    await ctx.edit_origin(content="Stocks bought!", components=[])
    # print("Squid game")
    await addAsset(ctx)

@slash.component_callback()
async def nobuy(ctx: ComponentContext):
    # await ctx.send()
    await ctx.edit_origin(content="Looks like we're not buying this.",components=[])
    await remBuy(ctx)

@client.command(name="market")
async def market(ctx, Stock):
    await markP(ctx, Stock, os.environ["key"])

@client.command(name="sell")
async def sell(ctx, Stock:Optional[str], Quant:Optional[str]):
    await sold(ctx, Stock, Quant, os.environ["key"])

@client.command(name="s")
async def s(ctx, Stock:Optional[str], Quant:Optional[str]):
    await sold(ctx, Stock, Quant, os.environ["key"])

@slash.component_callback()
async def yesell(ctx: ComponentContext):
    await ctx.edit_origin(content="Stocks sold!", components=[])
    # print("Squid game")
    await sellEm(ctx)

@slash.component_callback()
async def nosell(ctx: ComponentContext):
    # await ctx.send()
    await ctx.edit_origin(content="Looks like we're not selling these.",components=[])
    await remS(ctx)

@client.command(name="game")
async def game(ctx):
    await playing(ctx)

@client.command(name="leaderboard")
async def leaderboard(ctx):
    await winnin(ctx)

@client.command(name="lb")
async def lb(ctx):
    await winnin(ctx)
# print(os.environ["key"])
TOKEN = os.environ["token"]
client.run(TOKEN)