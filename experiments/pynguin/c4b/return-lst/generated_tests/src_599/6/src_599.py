def func(*args):
	ret_values = []
	
	(a, b) = map(int, list(args[0].split()))
	(c, d) = map(int, list(args[1].split()))
	for i in range(0, 1000):
	    for j in range(0, 1000):
	        if (((a * i) + b) == ((c * j) + d)):
	            ret_values.append(((a * i) + b))
	            exit(0)
	ret_values.append((- 1))

	return ret_values
