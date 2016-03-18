# from bs4 import BeautifulSoup
# from bs4 import Comment
# import re
# import urllib
import challengeFunction
import pickle

html = challengeFunction.get_challenge("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.loads(html)
data

# the output seems like a picture, so we should find a way to show the picture
# 数字代表字符的个数，把每一行展开，行与行之间擦入\n
print "\n".join([''.join([p[0]*p[1] for p in row]) for row in data])
