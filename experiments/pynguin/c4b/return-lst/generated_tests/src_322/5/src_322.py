def func(*args):
	ret_values = []
	
	cont = 0
	(n, a, b) = map(int, args[0].split())
	if ((a == 0) and (b == 0)):
	    ret_values.append(1)
	else:
	    for i in range(n):
	        if (((i - 1) <= b) and ((n - i) >= a)):
	            cont += 1
	    ret_values.append((cont - 1))

	return ret_values
