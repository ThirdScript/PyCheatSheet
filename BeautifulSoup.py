#!/usr/bin/python

# Importing The Main Function
from bs4 import BeautifulSoup
import urllib

# Fetch The Main HTML
_html = urllib.urlopen("http://instagram.com/google")

# We Make A BS Object Called Soup
# Now We Pass The Page Source Code IN To BeautiFul Soup
# We Use "LXML" Source Handler For Best Resualt
soup = BeautifulSoup(_html.read(), "lxml")

# To Get A Tag "soup.tag_name"
soup.h1
# To Access The Text Inside The Tag
soup.h1.string

# See The Main Tag Name
soup.h1.name

# Get The Meta Tag <Exmaple>
soup.meta
# See ONE Line After The Selected Tag
soup.meta.next

# Search For A Tag And Get All Founded Targets IN One Single List
soup.find_all("p")

# Get A Variable IN A Tag
# Like Access To "href" From "a" Tag
soup.find_all("a")[0]["href"]
# soup.find_all("a")[*]["href"]

