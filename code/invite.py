import discord


async def invited(ctx):
    invite_emb = discord.Embed(title="Inviting The Bot To Other Servers")
    invite_emb.add_field(name="Link:",value="[Click here to invite the bot to another server.](https://discord.com/oauth2/authorize?client_id=912180873208664064&permissions=3088&scope=bot)")
    await ctx.channel.send(embed=invite_emb)

