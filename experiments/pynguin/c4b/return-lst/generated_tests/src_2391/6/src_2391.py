def func(*args):
	ret_values = []
	
	input_nab = args[0].split()
	n = int(input_nab[0])
	a = int(input_nab[1])
	b = int(input_nab[2])
	front = (n - a)
	ret_values.append(min(front, (b + 1)))

	return ret_values
