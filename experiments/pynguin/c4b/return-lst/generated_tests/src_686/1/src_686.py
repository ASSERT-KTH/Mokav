def func(*args):
	ret_values = []
	
	s = (lambda x: ((x * (x + 1)) // 2))
	n = int(args[0])
	(lo, hi) = (0, (10 ** 10))
	while (lo != hi):
	    mid = (((lo + hi) + 1) // 2)
	    if (s(mid) < n):
	        lo = mid
	    else:
	        hi = (mid - 1)
	ret_values.append((n - s(lo)))

	return ret_values
