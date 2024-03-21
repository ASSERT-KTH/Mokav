def func(*args):
	ret_values = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	pages = v0
	if (pages >= c):
	    ret_values.append(1)
	else:
	    for i in range(1, 100000000):
	        pages -= l
	        pages += min((v0 + (i * a)), v1)
	        if (pages >= c):
	            ret_values.append((i + 1))
	            exit()

	return ret_values
