def func(*args):
	ret_values = []
	
	'input\n1358023\n'
	n = int(args[0])
	for x in range(((n // 1234567) + 1)):
	    for y in range(((n // 123456) + 1)):
	        if ((((n - (1234567 * x)) - (123456 * y)) >= 0) and ((((n - (1234567 * x)) - (123456 * y)) % 1234) == 0)):
	            ret_values.append('YES')
	            quit()
	ret_values.append('NO')

	return ret_values
