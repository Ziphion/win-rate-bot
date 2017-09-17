import praw
from praw.exceptions import APIException
from prawcore.exceptions import RequestException
from prawcore.exceptions import ServerError
import math
import datetime
import time
import re
import traceback
import wrbsecret
					
def post_reply(reply_md, mention):
	if hasattr(mention, 'permalink'):
		print("post_reply "+str(mention.permalink(fast=False)))
	else:
		print("post_reply")
	try:
		mention.reply(reply_md)
	except APIException as e:
		if e.error_type == 'RATELIMIT':
			print("Posting too fast: " + e.message)
			wait_time_m = int(re.search(r'\d+', e.message).group()) + 1
			if wait_time_m > 10:
				wait_time_m = 10
			print("going to sleep for "+ str(wait_time_m) + " minutes.")
			time.sleep(wait_time_m * 60)
			mention.reply(reply_md)
		else:
			raise e
		
def generate_reply(w, l):
	n = w+l
	p = (w+1)/(n+2)
	stdev = math.sqrt(p*(1-p)/(n+3))
	return(	"**Wins:** "+str(w)+"\n\n**Losses:** "+str(l)+
			"\n\nWith a sample size of "+str(n)+", I am about 70% certain that the win rate is **between "+str(round((p-stdev)*100,2))+"% and "+str(round((p+stdev)*100,2))+
			"%**.\n\n*****\n\n^I ^am ^a ^bot. [^About.](https://github.com/Ziphion/win-rate-bot/blob/master/README.md)")

		
def get_next_mention():
	for mention in bot.inbox.unread(limit=50):
		if not mention.new and not include_old_mentions:
			continue
		mention.mark_read()
		return mention

def get_wl(mention, regex):

	text = mention.body
	
	text.replace(" ","")
	match = re.search(regex, text.replace(" ", "").lower())
	if match:
		return int(match.group(1))
		

bot = praw.Reddit(	user_agent = 'win-rate-bot v0.1',
					client_id=wrbsecret.reddit_client_id,
					client_secret=wrbsecret.reddit_client_secret,
					username='win-rate-bot',
					password=wrbsecret.reddit_password)
					
include_old_mentions = False
sleep_time_s = 10

while True:
	try:
		mention = get_next_mention()
		
		if mention is None:
			time.sleep(sleep_time_s)
			continue
		w = get_wl(mention, 'w=(\d+)')
		l = get_wl(mention, 'l=(\d+)')
		if(w is not None and l is not None):
			reply_md = generate_reply(w, l)
	except (RequestException, ServerError):
		print("Exception "+str(datetime.datetime.utcnow()))
		time.sleep(30)
	else:
		try:
			if reply_md:
				post_reply(reply_md, mention)
		except Exception as e:
			print("Exception during post_reply:")
			print(e.__class__, e.__doc__)
			traceback.print_exc()