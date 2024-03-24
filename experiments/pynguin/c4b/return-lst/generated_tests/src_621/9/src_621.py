def func(*args):
	ret_values = []
	
	(n, x, y) = [int(i) for i in args[0].split()]
	ans = int((((y / 100) * n) - x))
	if (((ans + x) / n) < (y / 100)):
	    ans += 1
	if (ans > 0):
	    ret_values.append(ans)
	else:
	    ret_values.append(0)

	return ret_values
