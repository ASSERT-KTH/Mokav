def func(*args):
	ret_values = []
	
	x = args[0]
	test = '0'
	i = 0
	y = 0
	while (i < len(x)):
	    if (test == x[i]):
	        y += 1
	        if (y == 7):
	            ret_values.append('YES')
	            break
	    else:
	        y = 1
	        test = x[i]
	    i += 1
	else:
	    ret_values.append('NO')

	return ret_values
