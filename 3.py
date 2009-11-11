import re
from urllib.request import urlopen

target = re.compile('.*^[A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z]^[A-Z].*')

urldata = urlopen('http://www.pythonchallenge.com/pc/def/equality.html') 

print(target.match(urldata.read().decode()))
