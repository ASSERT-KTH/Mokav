def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	x = str(max(n, m))
	if (x == '1'):
	    ret_values.append('1/1')
	elif (x == '2'):
	    ret_values.append('5/6')
	elif (x == '3'):
	    ret_values.append('2/3')
	elif (x == '4'):
	    ret_values.append('1/2')
	elif (x == '5'):
	    ret_values.append('1/3')
	else:
	    ret_values.append('1/6')

	return ret_values
