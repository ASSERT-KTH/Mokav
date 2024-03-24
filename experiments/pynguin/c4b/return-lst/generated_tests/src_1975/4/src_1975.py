def func(*args):
	ret_values = []
	
	program_language = 'HQ9+'
	n = args[0]
	yes = []
	for el in n:
	    if ((el in program_language) and (el != '+')):
	        yes.append('1')
	if yes:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
