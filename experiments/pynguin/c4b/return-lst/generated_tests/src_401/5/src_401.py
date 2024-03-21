def func(*args):
	ret_values = []
	
	n = int(args[0])
	string = args[1]
	pages = list(map(int, string.split()))
	d = 0
	a = 0
	while (a < n):
	    a += pages[(d % 7)]
	    d += 1
	e = (d % 7)
	if (e == 0):
	    e = 7
	ret_values.append(e)

	return ret_values
