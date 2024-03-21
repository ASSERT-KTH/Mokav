def func(*args):
	ret_values = []
	
	(m, n) = map(int, args[0].split())
	(k, p) = map(int, args[1].split())
	l = 0
	if (((m - p) < 2) and ((p - m) < ((m + 1) * 2))):
	    l += 1
	if (((n - k) < 2) and ((k - n) < ((n + 1) * 2))):
	    l += 1
	if (l < 1):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
