def func(*args):
	ret_values = []
	
	n = int(args[0])
	res = int((n / 3))
	res *= 2
	if ((n % 3) > 0):
	    res += 1
	ret_values.append(res)

	return ret_values
