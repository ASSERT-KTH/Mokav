def original_func(*args):
	global_list = []
	
	(a, b) = (int(i) for i in args[0].split())
	t = 0
	if (a > b):
	    (a, b) = (b, a)
	while (b > 2):
	    x = ((b - 1) // 2)
	    t += x
	    a += x
	    b -= (2 * x)
	    (a, b) = (b, a)
	global_list.append((t + 1))
	return global_list