def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	l = ((m + n) - 3)
	if (((m - n) % 3) != 0):
	    l += 1
	ret_values.append(max(l, 0))

	return ret_values
