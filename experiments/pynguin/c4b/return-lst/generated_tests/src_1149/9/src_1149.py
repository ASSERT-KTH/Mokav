def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = args[1]
	x = (m.count('4') + m.count('7'))
	if (x != n):
	    ret_values.append('NO')
	elif (m[:(n // 2)].count('4') == m[(n // 2):].count('4')):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
