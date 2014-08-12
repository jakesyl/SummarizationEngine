from bs4 import BeautifulSoup#for getting uls from mobile site because python api is quite useless
import logging
import requests


#Creates Sandy Grey, the logger
logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff
logger = logging.getLogger(__name__)

def trendchaser():
	c=1#basically a counting variable, assuming the number of uls is a constant 10
	trends = []#an array for the different trends

	#Downloading and making the datareadable
	r  = requests.get("https://mobile.twitter.com/trends")#get's data from twitters trending page that the api doesn't provide
	page = r.text

	#Let's make some Beautiful Soup
	soup = BeautifulSoup(page)
	ul  = soup.find('ul') # Start here

	for li in ul:
		for li in ul.findAll('li'):
			trends.append(li)
	print trends
trendchaser()

'''
for nextSibling in sp.findNextSiblings():
	if nextSibling.name == 'a':
		break
		if nextSibling.name == 'li':.append(nextSibling)

			if li.find('ul'):
				break
				trends.append(li)
'''