def func(*args):
	ret_values = []
	
	x = args[0]
	x = int(x)
	for i in [4, 7, 47, 74, 447, 474, 477, 747, 774]:
	    if ((x % i) == 0):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
