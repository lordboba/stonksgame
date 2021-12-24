import discord
import aiofiles
import asyncio
import json
from aiohttp import ClientSession
import aiohttp
async def winnin(ctx, guild):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    chan = str(ctx.channel.id)
    Lb_emb = discord.Embed(title="Leaderboard", description= "These are the rankings by net worth. Note that leaderboards update approximately every hour.",color=0xFF5733,)
    sort_lb = sorted(data[chan]["LB"],key=data[chan]["LB"].get)
    sort_lb.reverse()
    # print(sort_lb)
    rank = 1
    for key in sort_lb:
        Lb_emb.add_field(name=f"{rank}. {guild.get_member(int(key)).name}", value=f"Net Worth: ${data[chan]['LB'][key]}", inline=False)
        rank = rank + 1
    await ctx.send(embed=Lb_emb)
    #data["LB"]

async def upd(key):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    data["Cache"] = {}
    #update net worth
    for chan in data["Games"]:
        
        for p in data[chan]["Players"]:
            net = data[chan]["PlayerData"][p]["Cash"]
            for stonk in data[chan]["PlayerData"][p]["Stocks"]:
                owned = (float)(data[chan]["PlayerData"][p]["Stocks"][stonk]["Num"])
                if stonk in data["Cache"]:
                    net = net + data["Cache"][stonk] *owned
                else:
                    headers = {"X-Finnhub-Token" : f"{key}"}
                    async with ClientSession() as session:
                        async with session.get(url=f"https://finnhub.io/api/v1/quote?symbol={stonk}",headers=headers) as response:
                            response.raise_for_status()
                            stock_info = await response.json()
                    data["Cache"][stonk] = stock_info["c"]
                    net = net + stock_info["c"] * owned
            data[chan]["PlayerData"][p]["NetWorth"] = net
            data[chan]["LB"][p] = net
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))

async def win2(id, channel,guild):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    # channel = await client.fetch_channel(id)
    chan = str(id)
    Lb_emb = discord.Embed(title="Leaderboard", description= "These are the final rankings by net worth.",color=0xBF40BF,)
    sort_lb = sorted(data[chan]["LB"],key=data[chan]["LB"].get)
    sort_lb.reverse()
    print(sort_lb)
    rank = 1
    for key in sort_lb:
        temp = guild.get_member(int(key))
        if temp == None:
            temp = id
        else:
            temp = temp.name
        Lb_emb.add_field(name=f"{rank}. {temp}", value=f"Net Worth: ${data[chan]['LB'][key]}", inline=False)
        rank = rank + 1
    await channel.send(embed=Lb_emb)