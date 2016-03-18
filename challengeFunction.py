from bs4 import BeautifulSoup
from bs4 import Comment
import urllib
import re
def get_challenge(url):
    html = urllib.urlopen(url).read()
    return html
    