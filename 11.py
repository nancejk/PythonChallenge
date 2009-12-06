from PIL import Image as im
o = im.open('cave.jpg')

# Open two new images of the same size.
n1 = im.new(o.mode,o.size)
n2 = im.new(o.mode,o.size)

# Grab the x and y maximum coords of the original
xmax, ymax = o.size[0], o.size[1]

# Iterate over ever pixel in the image, and decide if the product of the 
# coordinates is even or odd.  If it is even, add the pixel to one of the 
# images.  Otherwise, add it to the other.
for i in range(xmax):
	for j in range(ymax):
		if i*j % 2 == 0:
			n1.putpixel((i,j),o.getpixel((i,j)))
		if i*j % 2 == 1:
			n2.putpixel((i,j),o.getpixel((i,j)))

# Show both images (and look hard!)
n1.show()
n2.show()		   				