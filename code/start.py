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
    if time != None:
        time = time.upper()
        if (time[-1] != 'M' and time[-1] != 'D') or (not time[:-1].isnumeric):
            await ctx.send("Please send a valid value for time.")
            return

    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    if str(ctx.channel.id) in data:
        await ctx.send("There is already a game going on here. To start a new game, have a stonk-admin end the current game.")
    else:
        async with aiofiles.open('data.json', mode='r') as f:
            contents = await f.read()
        data = json.loads(contents)
        data["Starting"][str(ctx.channel.id)] = time
        async with aiofiles.open("data.json",'w') as out:
            await out.write(json.dumps(data))
        print(type(time))
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
    if data["Starting"][str(ctx.channel.id)] != None:
        #convert time to actual time
        temp = data["Starting"][str(ctx.channel.id)]
        temp = temp.upper()
        if temp[-1] == 'M':
            buffer = dt.timedelta(days=int(temp[:-1])*30)
        elif temp[-1] == 'D':
            buffer = dt.timedelta(days=int(temp[:-1]))
    data["Starting"].pop(str(ctx.channel.id))
    new = now+buffer
    data[ctx.channel.id] = {
        "Players" : [],
        "PlayerData" : {},
        "LB" : {},
        "EndTime" : new.strftime("%m/%d/%Y, %H:00"),
        "Buying" : {},
        "Selling" : {}
    }
    data["Games"].append(str(ctx.channel.id))
    # print(data)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))

async def no_st(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    chan = str(ctx.channel.id)
    data["Starting"].pop(chan)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))
