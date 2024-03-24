def func(*args):
	ret_values = []
	
	line = args[0].split()
	n = int(line[0])
	a = int(line[1])
	b = int(line[2])
	n -= a
	if (n > b):
	    n = (b + 1)
	ret_values.append(n)

	return ret_values
