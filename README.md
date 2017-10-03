# win-rate-bot
A reddit bot that takes a win-loss record for a game or contest and returns a range of win rates, taking into account the sample size.

I've noticed in communities for games like Hearthstone, a virtual card game, that players will claim that their decks have an enormous win rate (e.g. 75%+), but only a small sample size (e.g. 12 wins, 4 losses). In reality, it is dishonest to claim a win rate with a sample size that small, before you even get into factors such as day-to-day shifts in the player's aptitude or the distribution of opponents' decks (the "metagame"). With a small sample size, lucky or unlucky streaks are much more likely to throw off your average, giving you a win rate that is not the "true" win rate.

To call the bot (on any subreddit where it isn't banned), just mention /u/win-rate-bot and include a number of wins and losses, written as W = # and L = # (the bot does not care about upper/lowercase or spaces). You can also PM the bot or just reply to it without the mention; as long as it gets the notification, it will try to respond. Example:

> /u/win-rate-bot
> 
> w=12
> 
> l=4

This bot assumes a Beta distribution (https://en.wikipedia.org/wiki/Beta_distribution) for the range of possible values for the win rate (p), which will become a sharper and sharper peak as sample size increases:

> Pr{p|data} = (p^wins * (1-p)^losses)/(Beta(wins+1, losses+1))

To find the upper and lower bounds for the 95% confidence level, the bot uses the inverse cumulative distribution function at p=0.975 and p=0.025, respectively, where α = #wins + 1, β = #losses + 1. For 75% confidence, it uses p=0.875 and p=0.125.

Further reading:

Deriving the Beta distribution for an "unfair" coin flip: http://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html

Beta distributions in excel: http://www.real-statistics.com/binomial-and-related-distributions/beta-distribution/
