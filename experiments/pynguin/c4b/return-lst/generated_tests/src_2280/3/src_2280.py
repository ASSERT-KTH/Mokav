def func(*args):
	ret_values = []
	
	x = int(args[0])
	c = [4, 7, 47, 74, 444, 447, 477, 777, 744, 774, 777]
	a = 0
	for k in range(len(c)):
	    if ((x % c[k]) == 0):
	        a = 1
	        break
	if (a == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
