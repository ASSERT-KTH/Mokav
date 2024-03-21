def func(*args):
	ret_values = []
	
	a = args[0]
	b = args[1]
	c = args[2]
	d = ((a + b) + c)
	if (d == d[::(- 1)]):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
