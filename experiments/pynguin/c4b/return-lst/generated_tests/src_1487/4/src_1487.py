def func(*args):
	ret_values = []
	
	k = int(args[0])
	r = 0
	for i in range((k - 1)):
	    r += (((k - i) * (i + 1)) - i)
	ret_values.append((r + 1))

	return ret_values
