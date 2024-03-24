def func(*args):
	ret_values = []
	
	T = args[0]
	t = int(T)
	a = 0
	i = 0
	while (a < t):
	    a = ((i * (i + 1)) / 2)
	    i = (i + 1)
	if (t == 0):
	    ret_values.append('NO')
	elif (a == t):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
