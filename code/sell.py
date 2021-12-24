import discord
import os
import json
import aiofiles
import asyncio
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext
from aiohttp import ClientSession
import aiohttp
async def sold(ctx, Stock, Quant, key):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    chan = str(ctx.channel.id)
    id = str(ctx.author.id)
    if str(ctx.channel.id) not in data:
        await ctx.send("There is no game currently going on in this channel. To start a game, type in $start.")
    else:
        if Stock == "GEORGE" or Quant == "BOBBY" or Stock == None or Quant == None:
            await ctx.send("I'm sorry, you've likely inputted an invalid stock name or quantity. Please try again.")
        else:
            try:
                Quant = int(Quant)
            except ValueError:
                await ctx.send("Please send an integer value for the stock quantity bought.")
            else:
                if str(ctx.author.id) in data[str(ctx.channel.id)]["Players"]:
                    if Stock in data[chan]["PlayerData"][id]["Stocks"]:
                        if Quant > data[chan]["PlayerData"][id]["Stocks"][Stock]["Num"]:
                            await ctx.send(f"I'm sorry, you do not have that much {Stock} stock to sell. ")
                        else:
                            headers = {"X-Finnhub-Token" : f"{key}"}
                        
                            async with ClientSession() as session:
                                async with session.get(url=f"https://finnhub.io/api/v1/quote?symbol={Stock}",headers=headers) as response:
                                    response.raise_for_status()
                                    stock_info = await response.json()
                            price = (float(Quant)) * stock_info['c']
                            data[str(ctx.channel.id)]["Selling"][str(ctx.author.id)] = {"Stock":Stock, "Quant":Quant,"Price":price}
                            async with aiofiles.open("data.json",'w') as out:
                                await out.write(json.dumps(data))
                            await ctx.send(f"Do you want to sell {Quant} shares of {Stock} Stock for ${price}?", 
                            components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="yesell"), 
                            create_button(style=ButtonStyle.danger, label="No", custom_id="nosell"))])
                    else:
                        await ctx.send(f"I'm sorry, you do not own any of this stock. To buy some, do $buy {Stock} [Quantity]")
                    
                    
                else:
                    await ctx.send("You have not joined the game yet. Do you wish to join the game?", 
                    components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="yejoin"), 
                    create_button(style=ButtonStyle.danger, label="No", custom_id="nojoin"))])  

async def sellEm(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    chan = str(ctx.channel.id)
    id = str(ctx.author.id)
    info = data[chan]["Selling"][id]
    data[chan]["PlayerData"][id]["Cash"] = data[chan]["PlayerData"][id]["Cash"] + info["Price"]
    data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Num"] = data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Num"] - info["Quant"]
    if data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Num"] == 0:
        data[chan]["PlayerData"][id]["Stocks"].pop(info["Stock"])
    data[chan]["Selling"].pop(id)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))

async def remS(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    chan = str(ctx.channel.id)
    id = str(ctx.author.id)
    data[chan]["Selling"].pop(id)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))
    