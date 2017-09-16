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
	print("post_reply "+str(mention.permalink(fast=False)))
	try:
		mention.reply(reply_md)
	except APIException as e:
		#TODO
		raise e
		
def generate_reply(w, l):
	n = w+l
	p = w/n
	stdev = math.sqrt(p*(1-p)/n)
	return(	"**Wins:** "+str(w)+"\n\n**Losses:** "+str(l)+
			"\n\nI am about 70% certain that the win rate is **between "+str(round((p-stdev)*100,2))+"% and "+str(round((p+stdev)*100,2))+
			"%**.\n\n*****\n\n^I ^am ^a ^bot. [^About.](https://example.com)")

		
def get_next_mention():
	for mention in bot.inbox.mentions(limit=50):
		if not mention.new and not include_old_mentions:
			continue
		mention.mark_read()
		return mention

def get_wins(mention):

	text = mention.body
	
	text.replace(" ","")
	match = re.search('w=(\d+)', text.replace(" ", "").lower())
	if match:
		return int(match.group(1))
		

def get_losses(mention):

	text = mention.body
	
	text.replace(" ","")
	match = re.search('l=(\d+)', text.replace(" ", "").lower())
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
		w = get_wins(mention)
		l = get_losses(mention)
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