def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    n %= 4
	    res = 6
	    for i in range(1, (n + 1)):
	        res *= 8
	    ret_values.append((res % 10))

	return ret_values
