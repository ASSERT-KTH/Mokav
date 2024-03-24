def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ans = (n // 2)
	else:
	    ans = ((n + 1) // 2)
	ret_values.append(ans)

	return ret_values
