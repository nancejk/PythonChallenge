from urllib import urlopen
import math
from PIL import Image

urldata = urlopen('http://huge:file@www.pythonchallenge.com/pc/return/good.html')
readfirst = readsecond = False
first = ''
second = ''
for line in urldata.readlines():
	if 'first' in line and 'second' not in line:
		readfirst = True  
	if 'second' in line and 'first' not in line:
		readfirst = False
		readsecond = True
	if readfirst and not line.isspace() and 'first' not in line:
		first += line
	if readsecond and not line.isspace() and 'second' not in line:
		second += line 
	if line.isspace():
		readfirst = readsecond = False	
result = first+ ',' + second
final = ''
for char in result:
	if char.isdigit() or char is ',':
		 final += char

final = final.split(',')
zipped = zip([int(final[i]) for i in range(len(final)) if i % 2 == 0], [int(final[i]) for i in range(len(final)) if i % 2 == 1])

o = Image.open('/Users/nancejk/Desktop/good.jpg')
n = Image.new(o.mode,o.size)
for coord in zipped:
	n.putpixel(coord,(255,255,255))
	
n.show()