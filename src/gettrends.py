import logging
from twitter import *
from credentials import *#imports vars
#Creates Sandy Grey, the logger
logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
logger = logging.getLogger(__name__)

def trendchaser():
	try:
		t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))
	  # Get your "home" 

	except BaseException as exc:
		print str(exc)
trendchaser()