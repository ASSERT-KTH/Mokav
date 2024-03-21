def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	    exit()
	arr = [6, 8, 4, 2]
	ret_values.append(arr[(n % 4)])

	return ret_values
