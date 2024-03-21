def func(*args):
	ret_values = []
	
	x = int(args[0])
	c = 0
	for i in range(1, x):
	    if ((i % 2) == 0):
	        if (((x - i) % 2) == 0):
	            ret_values.append('YES')
	            c += 1
	            break
	if (c == 0):
	    ret_values.append('NO')

	return ret_values
