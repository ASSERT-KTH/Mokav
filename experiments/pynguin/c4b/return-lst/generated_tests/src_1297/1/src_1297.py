def func(*args):
	ret_values = []
	
	(a, b) = tuple(map(int, args[0].split()))
	(c, d) = tuple(map(int, args[1].split()))
	from sys import exit
	mod = (d % c)
	for i in range(1000):
	    if ((b >= d) and ((b % c) == mod)):
	        ret_values.append(b)
	        exit()
	    b += a
	ret_values.append((- 1))

	return ret_values
