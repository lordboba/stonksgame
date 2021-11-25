import discord
import aiofiles
import asyncio
import json
async def playing(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    chan = str(ctx.channel.id)
    if str(ctx.channel.id) not in data:
        await ctx.send("There is no game currently going on in this channel. To start a game, type in $start.")
    else:
        await ctx.send(f"Your game will end on {data[chan]['EndTime']} PST. Good luck!")
