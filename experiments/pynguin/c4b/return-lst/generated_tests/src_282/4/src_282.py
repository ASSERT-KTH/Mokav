def func(*args):
	ret_values = []
	
	from math import sqrt
	n = int(args[0])
	for i in range(1, 100):
	    if ((2 ** i) >= ((n / 5) + 1)):
	        a = (i - 1)
	        break
	c = int(((((n - (((2 ** a) - 1) * 5)) + (2 ** a)) - 1) / (2 ** a)))
	if (c == 1):
	    ret_values.append('Sheldon')
	elif (c == 2):
	    ret_values.append('Leonard')
	elif (c == 3):
	    ret_values.append('Penny')
	elif (c == 4):
	    ret_values.append('Rajesh')
	elif (c == 5):
	    ret_values.append('Howard')

	return ret_values
