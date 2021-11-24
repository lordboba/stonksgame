import discord
import aiofiles
import asyncio
from aiohttp import ClientSession
import aiohttp
async def markP(ctx, Stock, key):
    headers = {"X-Finnhub-Token" : f"{key}"}
    try:
        async with ClientSession() as session:
            async with session.get(url=f"https://finnhub.io/api/v1/quote?symbol={Stock}",headers=headers) as response:
                response.raise_for_status()
                stock_info = await response.json()
    except aiohttp.client_exceptions.ClientResponseError:
        await ctx.send("I'm sorry, you've likely specified an unknown or incorrect stock name. Please try again.")
    else:
        if stock_info['c'] == 0 and stock_info['d'] == None and stock_info['dp'] == None and stock_info['h'] == 0:
            await ctx.send("I'm sorry, you've likely specified an unknown or incorrect stock name. Please try again.")
        else:
            stock_emb = discord.Embed(title=f"{Stock} Stock Price")
            stock_emb.add_field(name="Current Price", value=f"${stock_info['c']}")
            await ctx.send(embed=stock_emb)
