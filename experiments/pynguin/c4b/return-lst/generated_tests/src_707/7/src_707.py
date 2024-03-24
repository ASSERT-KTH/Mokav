def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	(r, l) = map(int, args[1].split())
	for i in range(0, 101):
	    for j in range(101):
	        if (((a * i) + b) == (l + (r * j))):
	            ret_values.append(((a * i) + b))
	            exit()
	ret_values.append((- 1))

	return ret_values
