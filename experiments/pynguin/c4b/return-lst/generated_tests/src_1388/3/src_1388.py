def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = ((n // 3) * 2)
	if ((n % 3) != 0):
	    ans += 1
	ret_values.append(ans)

	return ret_values
