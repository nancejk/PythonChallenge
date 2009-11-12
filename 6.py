from zipfile import ZipFile
from re import compile

# We need this old guy again...
target = compile('Next nothing is ([0-9]{1,5})')

# Had to download this one.  Note that when I unzipped and 
# rezipped the file, this challenge step didn't work!
zobj = ZipFile('/Users/nancejk/Desktop/channel.zip','r')

# It says in the archive to start from 90052.
suffix = 90052

# The result will be a string, as usual.
result = ''
while True:
  objname = str(suffix) + '.txt'
  # Open the temporary file object from the zip archive.
  tempf = zobj.open(objname).read().decode()
  # As instructed, add the comment to the string.
  result += zobj.getinfo(objname).comment.decode()
  if target.match(tempf):
    # Look for the next target.
   suffix = target.match(tempf).groups(0)[0] 
   # Catch errors... and the ending.
  else:
    print(tempf)
    break

# Print out the result.  Note that you'll have to do just
# a little more work after you get it...
print(result)
