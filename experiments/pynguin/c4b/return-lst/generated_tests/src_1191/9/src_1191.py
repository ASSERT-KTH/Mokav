def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	min = ((n // 7) * 2)
	k = (n % 7)
	if (k > 4):
	    min += (k - 5)
	max = (n % 7)
	if (max > 2):
	    max = 2
	ret_values.append(min, (((n // 7) * 2) + max))

	return ret_values
