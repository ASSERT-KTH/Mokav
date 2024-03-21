def func(*args):
	ret_values = []
	
	import sys
	(n, k) = map(int, args[0].split())
	d = int((int((n / 2)) / (k + 1)))
	c = (k * d)
	if ((d >= 0) and (c >= 0) and ((c + d) <= int((n / 2)))):
	    ret_values.append(d, c, ((n - d) - c))
	else:
	    ret_values.append('0 0', n)

	return ret_values
