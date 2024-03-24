def func(*args):
	ret_values = []
	
	(l, r, k) = map(int, args[0].split())
	x = list(filter((lambda t: (l <= int(t) <= r)), [str((k ** i)) for i in range(256)]))
	if (len(x) == 0):
	    ret_values.append((- 1))
	else:
	    ret_values.append(' '.join(x))

	return ret_values
