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
async def afford(ctx, key, Stock="GEORGE", Quant="BOBBY"):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
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
                    headers = {"X-Finnhub-Token" : f"{key}"}
                    try:
                        async with ClientSession() as session:
                            async with session.get(url=f"https://finnhub.io/api/v1/quote?symbol={Stock}",headers=headers) as response:
                                response.raise_for_status()
                                stock_info = await response.json()
                    except aiohttp.client_exceptions.ClientResponseError:
                        await ctx.send("I'm sorry, you've likely inputted an unknown or incorrect stock name. Please try again.")
                    else:
                        if stock_info['c'] == 0 and stock_info['d'] == None and stock_info['dp'] == None and stock_info['h'] == 0:
                            await ctx.send("I'm sorry, you've likely inputted an unknown or incorrect stock name. Please try again.")
                        else:
                            price = (float(Quant)) * stock_info['c']
                            if price > data[str(ctx.channel.id)]["PlayerData"][str(ctx.author.id)]["Cash"]:
                                await ctx.send("I'm sorry, you do not have enough cash to buy this stock.")
                            else:
                                data[str(ctx.channel.id)]["Buying"][str(ctx.author.id)] = {"Stock":Stock, "Quant":Quant,"Price":price}
                                async with aiofiles.open("data.json",'w') as out:
                                    await out.write(json.dumps(data))
                                await ctx.send(f"Do you want to buy {Quant} shares of {Stock} Stock for ${price}?", 
                                components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="yebuy"), 
                                create_button(style=ButtonStyle.danger, label="No", custom_id="nobuy"))])
                    
                else:
                    await ctx.send("You have not joined the game yet. Do you wish to join the game?", 
                    components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="yejoin"), 
                    create_button(style=ButtonStyle.danger, label="No", custom_id="nojoin"))])  
            
async def addAsset(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    chan = str(ctx.channel.id)
    id = str(ctx.author.id)
    info = data[chan]["Buying"][id]
    data[chan]["PlayerData"][id]["Cash"] = data[chan]["PlayerData"][id]["Cash"] - info["Price"]
    
    if info["Stock"] in data[chan]["PlayerData"][id]["Stocks"]:
        data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Num"] = info["Quant"] + data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Num"]
    else:
        data[chan]["PlayerData"][id]["Stocks"][info["Stock"]] = {}
        data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Num"] = info["Quant"]
        data[chan]["PlayerData"][id]["Stocks"][info["Stock"]]["Init"] = info["Price"]/info["Quant"]
    data[chan]["Buying"].pop(id)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))

async def remBuy(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    chan = str(ctx.channel.id)
    id = str(ctx.author.id)
    data[chan]["Buying"].pop(id)
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))
    
