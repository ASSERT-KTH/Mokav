def func(*args):
	ret_values = []
	
	inStr = args[0]
	found = False
	if (inStr.find('H') != (- 1)):
	    found = True
	if (inStr.find('Q') != (- 1)):
	    found = True
	if (inStr.find('9') != (- 1)):
	    found = True
	if found:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
