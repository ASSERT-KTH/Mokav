def func(*args):
	ret_values = []
	
	(n, x, y) = map(int, args[0].split(' '))
	res = ((((x + y) % n) + n) % n)
	if (res == 0):
	    ret_values.append(n)
	else:
	    ret_values.append(res)

	return ret_values
