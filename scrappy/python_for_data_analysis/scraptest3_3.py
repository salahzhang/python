from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


parse = set()
random.seed(datetime.datetime.now())

#get the all list from internallink#
def getInternalLinks(bs0bj, includeUrl):
	includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
	internallinks = []
	#findall link begin with"/"#
	for link in bs0bj.findAll("a", href = re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internallinks:
				if (link.attrs['href'].startswith("/")):
					internallink.append(includeUrl+link.attrs['href'])
				else:
					internallink.append(link.attrs['href'])
	return internallinks


#get the all list from externallink#
def getExternalLinks(bs0bj, excludeUrl):
	# findall "http" and "www" without recent Url#
	externallinks = []
	for link in bs0bj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externallinks:
				externallinks.append(link.attrs['href'])
	return externallinks

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bs0bj = BeautifulSoup(html, "html.parser")
	externallinks = getExternalLinks(bs0bj, urlparse(startingPage).netloc)
	if len(externallinks) == 0:
		print("No external links, looking around the site for me")
		domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
		internallinks = getInternalLinks(bs0bj, domain)
		return getRandomExternalLink(internallinks[random.randint(0, len(internallinks) - 1)])
	else:
		return externallinks[random.randint(0, len(externallinks) - 1)]

def followExternalOnly(startingSite):
	externallink = getRandomExternalLink(startingSite)
	print("Random external link is"+externallink)
	followExternalOnly(externallink)

followExternalOnly("http://oreilly.com")


