### USING PYTHON 2.6 ###
from PIL import Image

# Open and load the image.
img = Image.open('/Users/nancejk/Desktop/oxygen.png')

xmax = img.size[0]
ymax = img.size[1]

# Traverse the image and look for the color plateau in x and y.
greyband_y = []
greyband_x = []

for value in range(ymax-1):
  if img.getpixel((0,value)) == img.getpixel((0,value+1)):
    greyband_y.append(value)

for value in range(xmax-1):
  if img.getpixel((value,greyband_y[0])) == img.getpixel((value+1,greyband_y[0])):
    greyband_x.append(value)

# This basically just forms a list comprehension of all of the pixels in
# the greyband_x, starting from 2 and then 9, 16, and so on (spaced by 7,
# which is the pixel width approximately).
greys = [img.getpixel((i,greyband_y[0]))[0] for i in [7*j + 2 for j in range(87)]]

# Convert the intensities to characters.
target = ''.join([chr(i) for i in greys])
print(target)

# The result is [105, 110, 116, 101, 103, 114, 105, 116, 121]
result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(i) for i in result]))
