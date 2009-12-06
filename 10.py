# This function takes an integer (or a stringified integer) and 'speaks' the
# integer e.g. 111 is 'three one', represented as '31'.

def speaknum(arg):
	temp = str(arg)
	result = ''
	index = 0
	count = 0
	while index < (len(temp)):
		char = temp[index]
		if index is not len(temp)-1:
			while index < len(temp)-1 and temp[index+1] is temp[index]: 
				count += 1
				index += 1
		result += (str(count+1) + char)
		count = 0
		index += 1
	return result

# start with '1', and for each iteration assign the result of speaknum(init)
# to init.  Rinse and repeat.
init = '1'
a = []
for iteration in range(40):
	a.append(len(init))
	init = speaknum(init)

# Here's the answer.
print(a[30])