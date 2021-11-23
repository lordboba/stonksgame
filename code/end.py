import discord
import aiofiles
import asyncio
import json
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext
async def endG(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    # print(data)
    # print(type(ctx.channel.id))
    if str(ctx.channel.id) not in data:
        await ctx.send("There is no game currently going on in this channel.")
    else:
        role = discord.utils.find(lambda r: r.name == 'stonk-admin', ctx.message.guild.roles)
        if role in ctx.author.roles:
            await ctx.send("Are you sure you want to end the current game in the channel?", 
        components=[create_actionrow(create_button(style=ButtonStyle.green, label="Yes", custom_id="ye_end"), 
        create_button(style=ButtonStyle.danger, label="No", custom_id="no_cont"))])
        else:
            await ctx.send("You need the stonk-admin role to execute this command. To do this, have an admin in your server create a role called 'stonk-admin' and assign it to you.")

async def shut_down(ctx):
    async with aiofiles.open('data.json', mode='r') as f:
        contents = await f.read()
    data = json.loads(contents)
    data.pop(str(ctx.channel.id))
    async with aiofiles.open("data.json",'w') as out:
        await out.write(json.dumps(data))
