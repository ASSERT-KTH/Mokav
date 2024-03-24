def func(*args):
	ret_values = []
	
	(k, l) = (int(args[0]), int(args[1]))
	(x, t) = (0, k)
	while (t < l):
	    t *= k
	    x += 1
	if (t == l):
	    ret_values.append('YES')
	    ret_values.append(x)
	else:
	    ret_values.append('NO')

	return ret_values
