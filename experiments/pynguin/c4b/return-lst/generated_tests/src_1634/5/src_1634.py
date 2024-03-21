def func(*args):
	ret_values = []
	
	(x1, y1, x2, y2) = [int(i) for i in args[0].split()]
	odd = (((y2 - y1) // 2) + 1)
	cnt = ((x2 - x1) // 2)
	ret_values.append(((odd * ((x2 - x1) + 1)) - cnt))

	return ret_values
