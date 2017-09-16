# win-rate-bot
A reddit bot that takes a win-loss record for a game or contest and returns a range of win rates, taking into account the sample size.

I've noticed in communities for games like Hearthstone, a virtual card game, that players will claim that their decks have an enormous win rate (e.g. 75%+), but only a small sample size (e.g. 12 wins, 4 losses). In reality, it is dishonest to claim a win rate with a sample size that small, before you even get into factors such as day-to-day shifts in the player's aptitude or the distribution of opponents' decks (the "metagame"). With a small sample size, lucky or unlucky streaks are much more likely to throw off your average, giving you a win rate that is not the "true" win rate.

This bot uses the standard deviation of the win rate to find an upper and lower bound, providing a range within which one can be 68.2% sure that the "actual" win rate (p) sits. The standard deviation is the square root of the variance in p over n trials, as given by the binomial distribution:

stdev = √(p*(1-p)/n)

If you have doubts about this, I've provided a "test" script (test_stdev.py) where you can verify this formula yourself with different values of p and n.

To call the bot (on any subreddit where it isn't banned), just mention /u/win-rate-bot and include a number of wins and losses, written as W = # and L = # (the bot does not care about upper/lowercase or spaces). Example:

  /u/win-rate-bot
  w=12
  l=4
