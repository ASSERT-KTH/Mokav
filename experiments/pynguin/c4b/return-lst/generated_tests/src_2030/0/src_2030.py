def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ans = ((n - 1) // 2)
	else:
	    ans = ((n // 2) - 1)
	ret_values.append(ans)

	return ret_values
