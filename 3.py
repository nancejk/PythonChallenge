import re
from urllib.request import urlopen

# The regex we will use for matching.
target = re.compile('[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]')

# Raw data from the page source.
urldata = urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode() 

# Grab just the data bit.
subset = urldata[urldata.find('!')+3:urldata.rfind('>')-2]

# Get rid of nasty newline characters introduced by decode.
subset = subset.replace('\n','')

# Print the answer.
print(''.join(re.findall(target,subset)))
