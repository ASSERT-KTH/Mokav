def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	if ((n % 2) == 1):
	    n -= 3
	    ret_values.append('7', end='')
	    for i in range((n // 2)):
	        ret_values.append('1', end='')
	else:
	    for i in range((n // 2)):
	        ret_values.append('1', end='')

	return ret_values
