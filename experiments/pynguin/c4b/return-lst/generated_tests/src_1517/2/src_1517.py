def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ans = int(((n / 2) - 1))
	else:
	    ans = int(((n - 1) / 2))
	ret_values.append(ans)

	return ret_values
