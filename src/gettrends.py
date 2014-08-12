import logging
from twitter import *

#Creates Sandy Grey, the logger
logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
logger = logging.getLogger(__name__)

def trendchaser():

t = Twitter(
    auth=OAuth(token, token_key, con_secret, con_secret_key)))
    # Get your "home" 
    home_timelint.statuses.home_timeline()