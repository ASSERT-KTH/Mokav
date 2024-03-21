def func(*args):
	ret_values = []
	
	(a, b) = (int(args[0]), int(args[1]))
	n = 0
	temp = a
	while (a < b):
	    a *= temp
	    n += 1
	if (a == b):
	    ret_values.append('YES')
	    ret_values.append(n)
	else:
	    ret_values.append('NO')

	return ret_values
