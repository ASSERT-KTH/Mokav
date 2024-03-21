def func(*args):
	ret_values = []
	
	import sys
	arr = list(map(int, args[0].split()))
	n = arr[0]
	a = arr[1]
	b = arr[2]
	c = arr[3]
	if ((n % 4) == 0):
	    ret_values.append(0)
	elif ((n % 4) == 3):
	    ret_values.append(min(a, (b + c), (c * 3), (c + (2 * a))))
	elif ((n % 4) == 2):
	    ret_values.append(min((a * 2), b, (c * 2), (c + (3 * a))))
	elif ((n % 4) == 1):
	    ret_values.append(min((a * 3), (b + a), c))

	return ret_values
