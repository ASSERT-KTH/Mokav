def func(*args):
	ret_values = []
	
	(y, k, n) = map(int, args[0].split())
	a = (k - (y % k))
	if ((y + a) <= n):
	    if (a == 0):
	        ret_values.append(' '.join((str(x) for x in [((t + 1) * k) for t in range(((n - y) // k))])))
	    else:
	        ret_values.append(' '.join((str(x) for x in [(a + (t * k)) for t in range((((n - y) // k) + 1)) if (((a + (t * k)) + y) <= n)])))
	else:
	    ret_values.append((- 1))

	return ret_values
