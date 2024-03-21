def func(*args):
	ret_values = []
	
	x = int(args[0])
	y = int(args[1])
	k = False
	u = 0
	for i in range(1, 32):
	    if (y == (x ** i)):
	        k = True
	        u = i
	        break
	if (k == False):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')
	    ret_values.append((u - 1))

	return ret_values
