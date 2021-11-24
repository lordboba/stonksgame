import discord


async def halp(ctx,set1,set2):
    if type(set1) == str:
        set1 = set1.lower()
    if type(set2) == str:
        set2 = set2.lower()
    help_emb = discord.Embed(title="Here are a list of commands for the StonksGame Bot.")
    if set1 == None or set1 == "help":
        help_emb.add_field(name="Help",value="$help, gives a list of commands that the bot can do")
    if set1 == None:
        help_emb.add_field(name = "Gameplay Mechanics",value="$help game, to learn more about the game mechanics behind the StonksGame Bot.")
    if set1 == None or set1 == "feedback" or set1 == "fb":
        help_emb.add_field(name="Feedback",value="$feedback, gives feedback to the developers.")
    if set1 == None or set1 == "invite" or set1 == "inv":
        help_emb.add_field(name="Invite",value="$invite, gives a link to invite the bot to other servers.")
    if set1 == "game":
        game_desc = ["$start [time year=Y month=M day=D], starts a trading game in the channel that lasts for the duration specified or by default 7 days(EX: $start 1M, starts a month-long game) Everyone in the game by default starts with $100000",
        "$end, ends the current game playing in the channel. Can only be used by people with the 'stonk-admin' role",
        "$join, allows to join if there is a current game in the channel",
        "$buy [4-Letter Stock Symbol] [Quantity], buys the amount of specified stock(EX: $buy TSLA 50, buys 50 Tesla Stock)",
        "$sell [4-Letter Stock Symbol] [Quantity], sells the amount of specified stock(EX: $sell TSLA 50, sells 50 Tesla Stock)",
        "$market [4-Letter Stock Symbol], returns a message giving the current market price of a stock(EX: $market TSLA, will give $1,137.06, as of 11/21/2021)",
        "$lb, gives the leaderboard of the Top 10 Traders according to net worth in the current game",
        "$assets, returns the player's current assets, including stocks owned"
        ]
        names = [["Start"],["End"],["Join"],["Buy","B"],["Sell","S"],["Market","M"],["Leaderboard","Lb"],["Assets"]]
        for i in range(len(names)):
            if set2 == None:
                help_emb.add_field(name=names[i][0],value=game_desc[i])
            for j in names[i]:
                if set2 == j.lower():
                    help_emb.add_field(name=names[i][0],value=game_desc[i])
    await ctx.channel.send(embed=help_emb)

