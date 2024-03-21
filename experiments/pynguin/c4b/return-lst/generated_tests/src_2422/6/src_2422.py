def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	for i in range(14):
	    if ((a % b[i]) == 0):
	        ret_values.append('YES')
	        a = 0
	        break
	if (a != 0):
	    ret_values.append('NO')

	return ret_values
