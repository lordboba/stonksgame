import discord
import json
import aiofiles

async def items(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    if str(ctx.channel.id) not in data:
        await ctx.send("There is no game currently going on in this channel. To start a game, type in $start.")
    else:
        channel = str(ctx.channel.id)
        user = str(ctx.author.id)
        if user not in data[channel]["Players"]:
            await ctx.send("You have not joined the current game yet. Type $join to join the game.")
        else:
            item_emb = discord.Embed(title="Your Current Assets")
            currD = data[channel]["PlayerData"][user]
            item_emb.add_field(name="Cash",value=f"${currD['Cash']}")
            for key in currD["Stocks"]:
                init = currD['Stocks'][key]['Init']
                item_emb.add_field(name=key,value=f"{currD['Stocks'][key]['Num']}, Initial Buy Price ${init} {('',(':chart_with_upwards_trend:',':chart_with_downwards_trend:')[data['Cache'][key]>init])[key in data['Cache']]}")
            item_emb.add_field(name="Net Worth",value=f"${currD['NetWorth']}(Note that this is updated every hour.)",inline=False)
            await ctx.send(embed=item_emb)
