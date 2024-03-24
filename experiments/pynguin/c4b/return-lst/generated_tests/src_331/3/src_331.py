def func(*args):
	ret_values = []
	
	l = list(map(int, args[0].split(' ')))
	a = l[0]
	b = l[1]
	c = l[2]
	d = (b - a)
	if (d == 0):
	    ret_values.append('YES')
	elif (c != 0):
	    if (((d % c) == 0) and ((d * c) > 0)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
