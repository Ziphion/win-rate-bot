# win-rate-bot
A reddit bot that takes a win-loss record for a game or contest and returns a range of win rates, taking into account the sample size.

I've noticed in communities for games like Hearthstone, a virtual card game, that players will claim that their decks have an enormous win rate (e.g. 75%+), but only a small sample size (e.g. 12 wins, 4 losses). In reality, it is dishonest to claim a win rate with a sample size that small, before you even get into factors such as day-to-day shifts in the player's aptitude or the distribution of opponents' decks (the "metagame"). With a small sample size, lucky or unlucky streaks are much more likely to throw off your average, giving you a win rate that is not the "true" win rate.

This bot uses the standard deviation of the win rate to find an upper and lower bound, providing a range within which one can be 68.2% sure that the "actual" win rate sits. The best estimate you can make for the actual win rate (let's call it "p") is the value that sits right in the middle of that range, and it depends on n:

> p = (w+1)/(n+2)

(w = wins). Why is this not w/n? Because for low n, w/n does not represent the middle of the range of likely win rates for that win/loss record. For example, if I have 2 wins 0 losses, using w/n gives you 100%, but that isn't in the middle of our possible range; an actual win rate could easily be 75%, 50%, etc.

We get the upper and lower bounds by adding and subtracting the standard deviation to the average p we calculated above. The standard deviation is given by:

> stdev = √(p*(1-p)/(n+3))

If you have doubts about these values for p and stdev, I've provided a "test" script (test_stdev.py) where you can verify this formula yourself with different values for wins and losses.

To call the bot (on any subreddit where it isn't banned), just mention /u/win-rate-bot and include a number of wins and losses, written as W = # and L = # (the bot does not care about upper/lowercase or spaces). Example:

> /u/win-rate-bot
> 
> w=12
> 
> l=4
