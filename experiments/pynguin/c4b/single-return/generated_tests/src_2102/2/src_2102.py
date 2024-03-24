def func(*args):
	
	from math import ceil
	a = args[0]
	b = a.split()
	return((ceil((float(b[0]) / float(b[2]))) * ceil((float(b[1]) / float(b[2])))))
