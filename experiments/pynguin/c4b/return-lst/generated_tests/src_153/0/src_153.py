def func(*args):
	ret_values = []
	
	'input\n3\n8\n'
	(k, l) = (int(args[0]), int(args[1]))
	for x in range(1, 100):
	    if ((k ** x) == l):
	        ret_values.append('YES')
	        ret_values.append((x - 1))
	        break
	else:
	    ret_values.append('NO')

	return ret_values
