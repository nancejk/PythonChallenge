import pickle
from urllib.request import urlopen

# In the source it makes reference to a banner.p file.
floc = 'http://www.pythonchallenge.com/pc/def/banner.p'
urldata = urlopen(floc).read()

# Let's unpickle it.
target = pickle.loads(urldata)

for line in target:
  str = ''
  # Treat it like a RLE.
  for tuple in line:
    str += tuple[0]*tuple[1]
  # Each line contributes to the result.
  print(str)

