import discord
import aiofiles
import asyncio
import json
async def winnin(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    chan = str(ctx.channel.id)
    Lb_emb = discord.Embed(title="Leaderboard", description= "These are the rankings by net worth. Note that leaderboards update approximately every hour.",color=0xFF5733,)
    sort_lb = sorted(data[chan]["LB"],key=data[chan]["LB"].get)
    rank = 1
    for key in sort_lb:
        Lb_emb.add_field(name=f"{rank}. <@{key}>", value=f"Net Worth: ${data[chan]['LB'][key]}", inline=False)
        rank = rank + 1
    await ctx.send(embed=Lb_emb)
    #data["LB"]

