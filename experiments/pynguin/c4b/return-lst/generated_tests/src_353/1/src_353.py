def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = 0
	if ((a % 5) == 0):
	    b = (- 1)
	ret_values.append((((a // 5) + 1) + b))

	return ret_values
