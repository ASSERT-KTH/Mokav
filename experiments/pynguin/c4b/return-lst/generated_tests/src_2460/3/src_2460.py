def func(*args):
	ret_values = []
	
	x = args[0].split()
	y = []
	for i in x:
	    y.append(int(i))
	z = 1
	for i in range(5):
	    if ((3 * y[0]) <= (2 * y[1])):
	        z = (z + 1)
	        y[0] = (y[0] * 3)
	        y[1] = (y[1] * 2)
	ret_values.append(z)

	return ret_values
