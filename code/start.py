import discord
from typing import Optional
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext
import json
import aiofiles
import asyncio
import datetime as dt
async def st(ctx, time:Optional[str]):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    if str(ctx.channel.id) in data:
        await ctx.send("There is already a game going on here. To start a new game, have a stonk-admin end the current game.")
    else:
        await ctx.send("Are you sure you want to start a stonk trading game here?", 
        components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="yea"), 
        create_button(style=ButtonStyle.danger, label="No", custom_id="nou"))])

async def create_game(ctx):
    # print("oi")
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    print(type(ctx.channel.id))
    # print("hi")
    now = dt.datetime.now()
    buffer = dt.timedelta(weeks=1)
    new = now+buffer
    data[ctx.channel.id] = {
        "Players" : [],
        "PlayerData" : {},
        "LB" : {},
        "EndTime" : new.strftime("%m/%d/%Y, %H:%M")
    }
    # print(data)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))
