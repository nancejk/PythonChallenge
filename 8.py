from urllib import urlopen
import bz2 
import re

# A regex to match the username string
uname = re.compile('un: (.+)')
pword = re.compile('pw: (.+)')

urldata = urlopen('http://www.pythonchallenge.com/pc/def/integrity.html')
for line in urldata:
  sline = str(line)
  if uname.match(sline):
    un = uname.match(sline).groups(0)[0]
  if pword.match(sline):
    pw = pword.match(sline).groups(0)[0]

print("un: " + bz2.decompress(eval("" + un + "")))
print("pw: " + bz2.decompress(eval("" + pw + "")))
