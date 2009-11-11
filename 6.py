from zipfile import ZipFile

zobj = ZipFile('/Users/nancejk/Desktop/channel.zip','r')

basename = 'channel/'
# It says in the archive to start from 90052.
first = 90052

while True:
  temp = zobj.open(basename + str(first) + '.txt')
  print(temp.read())



