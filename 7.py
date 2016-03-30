import challengeFunction
import os
## read html
html = challengeFunction.get_challenge("http://www.pythonchallenge.com/pc/def/channel.html")
os.chdir("channel/")
f = open("90052.txt", "r")
content = f.read()
next = content[16:]
input = next+".txt"
fileList = ["90052.txt"]
for i in range(1000):
    f = open(input,"r")
    content = f.read()
    next = content[16:]
    input = next+".txt"
    fileList.append(input)
    print content

for file in os.listdir('.'):
    if file not in fileList:
        print file


# Collect the comments
os.stat("90052.txt")

