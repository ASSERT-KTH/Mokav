def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	c = 1
	while (((l / k) != 1) and ((l - k) > 0) and (l != 1)):
	    l /= k
	    c += 1
	if ((l / k) == 1):
	    ret_values.append('YES')
	    ret_values.append((c - 1))
	else:
	    ret_values.append('NO')

	return ret_values
