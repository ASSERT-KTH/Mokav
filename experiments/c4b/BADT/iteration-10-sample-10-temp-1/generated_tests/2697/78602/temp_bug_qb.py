def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	res = (- 1)
	k = 0
	while ((k < a) and (res == (- 1))):
	    if ((((d + (k * c)) - b) % a) == 0):
	        res = (d + (k * c))
	    k += 1
	global_list.append(res)
	return global_list