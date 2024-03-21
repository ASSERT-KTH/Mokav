def func(*args):
	ret_values = []
	
	x = args[0]
	i = 0
	z = ''
	for i in range((len(x) - 6)):
	    if ((str(x[i]) == str(x[(i + 1)])) and (str(x[i]) == str(x[(i + 2)])) and (str(x[i]) == str(x[(i + 3)])) and (str(x[i]) == str(x[(i + 4)])) and (str(x[i]) == str(x[(i + 5)])) and (str(x[i]) == str(x[(i + 6)]))):
	        z = 0
	    i += 1
	if (z == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
