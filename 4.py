from urllib.request import urlopen 
from re import compile, match

# This is the base url.  To form a url with data, we need to append
# a number to it.
baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

# The regular expression that will get the numbers out of the
# appropriate text.
target = compile('.+ the next nothing is ([0-9]{1,5})')

# The initial url appendage
nothing = 12345

# Loop forever.  We will break out when we reach the end of the linked
# steps.
while True:
# Compose the target url and strip out newline characters that will
# confuse our regex engine.
  urldata = urlopen(baseurl + str(nothing)).read().decode().replace('\n','')
  match = target.match(urldata)
# If there is a regex match, use the new number as nothing and proceed.
  if match:
    nothing = match.groups(0)[0]
# Avoids a wrench in the works.
  if 'Divide by two' in urldata:
    nothing = int(nothing)/2
# If there's not a match to the regular expression, print what the URL
# says and break out of the forever loop.
  elif not match:
    print(urldata)
    break
