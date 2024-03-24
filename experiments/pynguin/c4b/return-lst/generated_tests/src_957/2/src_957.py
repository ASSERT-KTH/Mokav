def func(*args):
	ret_values = []
	
	(n, k) = list(map(int, args[0].split()))
	ans = ((n * (n - 1)) // 2)
	if (k >= (n // 2)):
	    ret_values.append(ans)
	else:
	    m = (n - (2 * k))
	    ans = (ans - ((m * (m - 1)) // 2))
	    ret_values.append(ans)

	return ret_values
