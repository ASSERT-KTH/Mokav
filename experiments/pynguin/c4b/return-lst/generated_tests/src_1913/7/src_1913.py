def func(*args):
	ret_values = []
	
	import math
	(m, d) = map(int, args[0].split())
	if ((m < 8) and ((m % 2) == 1)):
	    c = 31
	elif (m == 2):
	    c = 28
	elif (m < 8):
	    c = 30
	elif ((m >= 8) and ((m % 2) == 0)):
	    c = 31
	else:
	    c = 30
	l = (8 - d)
	c -= l
	ret_values.append((math.ceil((c / 7)) + 1))

	return ret_values
