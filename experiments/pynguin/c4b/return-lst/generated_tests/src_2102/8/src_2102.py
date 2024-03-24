def func(*args):
	ret_values = []
	
	from math import ceil
	a = args[0]
	b = a.split()
	ret_values.append((ceil((float(b[0]) / float(b[2]))) * ceil((float(b[1]) / float(b[2])))))

	return ret_values
