def func(*args):
	
	input_nab = args[0].split()
	n = int(input_nab[0])
	a = int(input_nab[1])
	b = int(input_nab[2])
	front = (n - a)
	return(min(front, (b + 1)))
