# stonksgame
StonksGame:
A Discord Bot for hosting live stock trading simulation contests. Bot Prefix: $
Command/Categories:
1. help - $help, gives a list of commands that the bot can do
2. game - Mechanics of Gameplay
  i. start - $start [time year=Y month=M day=D],  starts a trading game in the channel that lasts for the duration specified or by default 7 days(EX: $start 1M)
  ii. end - $end, ends the current game playing in the channel. Can only be used by people with the "stonk-admin" role
  iii. buy/b - $buy [4-Letter Stock Symbol] [Quantity], buys the amount of specified stock(EX: $buy TSLA 50, buys 50 Tesla Stock )
  iv. market/m - $market [4-Letter Stock Symbol], returns a message giving the current market price of a stock(EX: $market TSLA, will give $1,137.06, as of 11/21/2021)
  v. leaderboard/lb - $lb, gives the leaderboard of the Top 10 Traders according to net worth in the current game
  vi. assets - $assets, returns the player's current assets, including stocks owned and net wroth
3. feedback - $feedback, gives feedback to the developers
