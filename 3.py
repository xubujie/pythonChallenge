from bs4 import BeautifulSoup
from bs4 import Comment
import urllib
html = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
soup = BeautifulSoup(html,"html.parser")
# get Comment of the page
comments=soup.findAll(string=lambda text:isinstance(text,Comment))
input = comments[1]

# check the set of input
inputSet = set(input)
[input.count(a) for a in inputSet]
output = "aeilqtuy"
for i in input:
    if i in output:
        print i
