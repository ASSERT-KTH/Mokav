def func(*args):
	ret_values = []
	
	mas = args[0]
	if ((mas.count('1111111') > 0) or (mas.count('0000000') > 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
