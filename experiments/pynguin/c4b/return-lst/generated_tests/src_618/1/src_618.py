def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	aa = []
	for i in range(0, 10):
	    for j in range(0, 10):
	        for k in range(0, 10):
	            if (((((n + i) + (j * 2)) + (k * 3)) % 4) == 0):
	                aa.append((((a * i) + (b * j)) + (c * k)))
	ret_values.append(min(aa))

	return ret_values
