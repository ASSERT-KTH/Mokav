def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	(x, y, z) = map(int, args[1].split())
	pos = 0
	neg = 0
	if (a > x):
	    pos += ((a - x) // 2)
	else:
	    neg += (x - a)
	if (b > y):
	    pos += ((b - y) // 2)
	else:
	    neg += (y - b)
	if (c > z):
	    pos += ((c - z) // 2)
	else:
	    neg += (z - c)
	if (pos >= neg):
	    ret_values.append('Yes')
	else:
	    ret_values.append('No')

	return ret_values
