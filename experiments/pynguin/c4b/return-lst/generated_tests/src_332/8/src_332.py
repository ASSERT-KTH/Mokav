def func(*args):
	ret_values = []
	
	l = list(map(int, args[0].split(' ')))
	t = l[0]
	s = l[1]
	x = l[2]
	if (x == t):
	    ret_values.append('YES')
	elif (((((x - t) % s) == 0) and ((x - t) > 0)) or (((((x - t) - 1) % s) == 0) and (((x - t) - 1) > 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
