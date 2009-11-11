from urllib.request import urlopen
import re

# This is the url containing the target mess.
baseurl='http://www.pythonchallenge.com/pc/def/ocr.html'

# A regular expression to match the comments.
comment = re.compile('\<\!\-\-')

# The string containing the contents of the url.
urldata = urlopen(baseurl).read().decode()

# Find the first '%' character and the last '>' character.
# in between is the prize up to some hyphens (we subtract 2
# to take care of them)
target = urldata[urldata.find('%'):urldata.rfind('>')-2]

# The hint says to find the 'rare characters'.  Because everything
# else is special characters, it's a fair guess that they are talking
# about letters.  so we'll pull the same trick we did in p.1 and
# do this alphanumerically.
Alphas = [chr(i) for i in range(65,91)]
alphas = [chr(i) for i in range(97,123)]

result = ''
for char in target:
# If it's alphanumeric, store it.
  if char in Alphas or char in alphas:
    result += char

# Here's the answer.
print(result)
