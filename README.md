# stonksgame
StonksGame: A Discord Bot for hosting live stock trading simulation contests. Bot Prefix: $

Commands/Categories:

1. help - $help, gives a list of commands that the bot can do
2. game - Mechanics of Gameplay
    1. start - $start [time month=M day=D],  starts a trading game in the channel that lasts for the duration specified or by default 7 days(EX: $start 1M, starts a month-long game)
    2. end - $end, ends the current game playing in the channel. Can only be used by people with the "stonk-admin" role
    3. join - $join, allows to join if there is a current game in the channel
    4. buy/b - $buy [4-Letter Stock Symbol] [Quantity], buys the amount of specified stock(EX: $buy TSLA 50, buys 50 Tesla Stock)
    5. sell/s - $sell [4-Letter Stock Symbol] [Quantity], sells the amount of specified stock(EX: $sell TSLA 50, sells 50 Tesla Stock)
    6. market/m - $market [4-Letter Stock Symbol], returns a message giving the current market price of a stock(EX: $market TSLA, will give $1,137.06, as of 11/21/2021)
    7. leaderboard/lb - $lb, gives the leaderboard of the Top 10 Traders according to net worth in the current game
    8. assets - $assets, returns the player's current assets, including stocks owned
3. feedback - $feedback, gives feedback to the developers, done in DMs
4. invite - $invite, gives link to invite the bot to other servers
