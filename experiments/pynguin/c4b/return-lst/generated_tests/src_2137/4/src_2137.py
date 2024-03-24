def func(*args):
	ret_values = []
	
	a = args[0]
	b = args[1]
	c = args[2]
	d = 0
	if (a[0] != c[2]):
	    d += 1
	if (a[1] != c[1]):
	    d += 1
	if (a[2] != c[0]):
	    d += 1
	if (b[0] != b[2]):
	    d += 1
	if (d == 0):
	    ret_values.append('YES')
	if (d != 0):
	    ret_values.append('NO')

	return ret_values
