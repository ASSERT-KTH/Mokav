def func(*args):
	ret_values = []
	
	a = [int(i) for i in args[0].split()]
	if (((a[0] - a[1]) >= (- 1)) and ((a[0] - a[1]) <= 1) and ((a[1] > 0) or (a[0] > 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
