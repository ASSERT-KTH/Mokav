def func(*args):
	ret_values = []
	
	import math
	n_x_y = list(map(int, args[0].split()))
	minn = math.ceil(((n_x_y[2] / 100) * n_x_y[0]))
	req = (minn - n_x_y[1])
	if (req < 0):
	    ret_values.append('0')
	else:
	    ret_values.append(req)

	return ret_values
