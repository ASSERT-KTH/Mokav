def func(*args):
	ret_values = []
	
	i = args[0]
	(n, s) = (int(i[:(- 1)]), i[(- 1)])
	t = (16 * ((n - 1) // 4))
	n %= 4
	if (n == 0):
	    n += 4
	if ((n == 1) or (n == 3)):
	    ret_values.append(((t + 'fedabc'.index(s)) + 1))
	else:
	    ret_values.append(((t + 'fedabc'.index(s)) + 8))

	return ret_values
