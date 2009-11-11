from zipfile import ZipFile
from re import compile

target = compile('Next nothing is ([0-9]{1,5})')
zobj = ZipFile('/Users/nancejk/Desktop/channel.zip','r')
basename = 'channel/'
# It says in the archive to start from 90052.
suffix = 90052

while True:
  temp = zobj.open(basename + str(suffix) + '.txt').read().decode()
  if target.match(temp):
   suffix = target.match(temp).groups(0)[0] 
   print(temp, suffix)
  else:
    print(temp)
    break
  

