import discord
import asyncio
import os

async def dev_fb(ctx, client):
    await ctx.channel.send("Read the DM that I sent you.")
    
    embed = discord.Embed(title="Hello, and thanks for using the StonksGame Bot!")
    embed.add_field(name="How To Send Feedback", value="Please write what you want to send to the creator of this discord bot. Please be mindful of what you send. You have 5 minutes.")
    dm_msg = await ctx.author.send("Hi!")
    await dm_msg.channel.send(embed=embed)
    def check(m):
        return m.channel == dm_msg.channel and m.author != client.user
    try:
        feed_back = await client.wait_for('message', check=check, timeout=300.0)
    except asyncio.TimeoutError:
        await dm_msg.channel.send("I'm sorry, but your feedback session has timed out.")
    else:
        dev_1 = await ctx.bot.fetch_user(int(os.environ['nerd_1']))
        await dev_1.send(f"{ctx.author.name} says: {feed_back.content}")
    