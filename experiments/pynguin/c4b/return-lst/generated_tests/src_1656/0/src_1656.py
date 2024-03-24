def func(*args):
	ret_values = []
	
	(n, k) = [int(i) for i in args[0].split()]
	if (k >= (n // 2)):
	    ret_values.append(((n * (n - 1)) // 2))
	else:
	    ans = (((((n - 1) + n) - k) * k) // 2)
	    ans = ((ans * 2) - (k * k))
	    ret_values.append(ans)

	return ret_values
