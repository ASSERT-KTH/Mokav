def func(*args):
	ret_values = []
	
	x = [int(y) for y in args[0]]
	i = 0
	q = 0
	while (i < len(x)):
	    if ((x[i] == 7) or (x[i] == 4)):
	        q += 1
	    i += 1
	if ((q == 4) or (q == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
