def func(*args):
	ret_values = []
	
	n = args[0]
	a = (n.count('4') + n.count('7'))
	if (((a == 4) or (a == 7)) and (a != 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
