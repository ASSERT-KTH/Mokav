def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = 0
	if ((n % 2) == 0):
	    ans = (n // 4)
	    if ((n % 4) == 0):
	        ans -= 1
	ret_values.append(ans)

	return ret_values
