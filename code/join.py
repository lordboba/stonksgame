import discord
import json
import aiofiles
import asyncio
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext

async def joined(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    if str(ctx.channel.id) not in data:
        await ctx.send("There is no game currently going on in this channel. To start a game, type in $start.")
    else:
        if str(ctx.author.id) in data[str(ctx.channel.id)]["Players"]:
            await ctx.send("You have already joined the game.")
        else:
            await ctx.send("Do you want to join the current StonkGame?", 
            components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="yejoin"), 
            create_button(style=ButtonStyle.danger, label="No", custom_id="nojoin"))])

async def add_user(ctx):
    id = str(ctx.author.id)
    channel = str(ctx.channel.id)
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    data[channel]["Players"].append(id)
    player = {
        "NetWorth" : 100000.0,
        "Stocks": {},
        "Cash": 100000.0
    }
    data[channel]["PlayerData"][id] = player
    data[channel]["LB"][id] = 100000.0
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))
