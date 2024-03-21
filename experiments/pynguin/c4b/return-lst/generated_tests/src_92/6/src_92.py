def func(*args):
	ret_values = []
	
	(n, m, l, r, k) = map(int, args[0].split())
	x = max(n, l)
	y = min(m, r)
	l = ((y - x) + 1)
	if ((x <= k) and (k <= y)):
	    l -= 1
	ret_values.append(max(0, l))

	return ret_values
