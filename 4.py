from bs4 import BeautifulSoup
from bs4 import Comment
import urllib
import re
html = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
soup = BeautifulSoup(html,"html.parser")
comments=soup.findAll(string=lambda text:isinstance(text,Comment))
input = comments[0]
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
# pattern = "EXACTLY*EXACTLY"
p = "[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]"

# find pattern p in input string
match = re.findall(p, input)
outPut = ""
for a in match:
    outPut = outPut + a[4];
print outPut


