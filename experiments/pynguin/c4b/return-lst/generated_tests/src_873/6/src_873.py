def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	i = 0
	while (a <= b):
	    i += 1
	    a = (a * 3)
	    b = (b * 2)
	    if (a > b):
	        ret_values.append(i)
	        break

	return ret_values
