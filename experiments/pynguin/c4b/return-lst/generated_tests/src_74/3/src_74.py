def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = 0
	while ((k ** m) < l):
	    m = (m + 1)
	if ((k ** m) > l):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')
	    ret_values.append((m - 1))

	return ret_values
