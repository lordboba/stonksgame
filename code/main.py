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
from leaderboard import winnin, upd, win2
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext
import aiofiles
import json
from aiohttp import ClientSession

# print("hi my name is bob")
load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', activity=discord.Game(name="Playing $help"),intents=intents)
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
    guild = client.get_guild(ctx.guild.id)
    await winnin(ctx, guild)

@client.command(name="lb")
async def lb(ctx):
    guild = client.get_guild(ctx.guild.id)
    await winnin(ctx, guild)

@tasks.loop(hours=1)
async def my_task():
    #update leaderboard and check for completed games
    await upd(os.environ["key"])
    #now check for ending games
    #ends game that run out of time
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    rem = []
    for chan in data["Games"]:
        e_time = dt.datetime.strptime(data[chan]["EndTime"],"%m/%d/%Y, %H:%M")
        now  = dt.datetime.now()
        if now > e_time:
            channel = await client.fetch_channel(chan)
            await channel.send("Game Over! Here are the final results of the game. Congrats to the Winners!")
            guild = client.get_guild(channel.guild.id)
            await win2(chan,channel,guild)
            rem.append(chan)
    
    #remove finished games
    for chan in rem:
        data.pop(chan)
        data["Games"].remove(chan)

    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))



@my_task.before_loop
async def before_my_task():
    hour = 12
    minute = 00
    #print("hiafwefaweff")
    await client.wait_until_ready()
    #print("hiawefawfafafefdhiawewafahiwdheafefadwihafahidiedfdaifeafida")
    now = dt.datetime.now()
    #print(now)
    future = dt.datetime(now.year, now.month, now.day, hour, minute)
    # print(future)
    if now.hour >= hour and now.minute > minute:
        future += dt.timedelta(days=1)
    print((future-now).seconds)
    await asyncio.sleep((future-now).seconds)

# print(os.environ["key"])
my_task.start()
TOKEN = os.environ["token"]
client.run(TOKEN)