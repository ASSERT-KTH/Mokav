def original_func(*args):
	global_list = []
	
	(n, a, b) = [int(i) for i in args[0].split()]
	t = 0
	for i in range(n):
	    if ((i >= a) and (i <= b)):
	        t += 1
	global_list.append((t + 1))
	return global_list