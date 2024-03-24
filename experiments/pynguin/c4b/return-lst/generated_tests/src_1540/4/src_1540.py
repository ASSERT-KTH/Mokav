def func(*args):
	ret_values = []
	
	string = args[0]
	code = 'HQ9'
	for i in string:
	    if (i in code):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
