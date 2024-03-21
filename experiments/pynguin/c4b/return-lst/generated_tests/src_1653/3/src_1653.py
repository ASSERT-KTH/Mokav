def func(*args):
	ret_values = []
	
	n = args[0]
	for i in n:
	    if (i in {'H', 'Q', '9'}):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
