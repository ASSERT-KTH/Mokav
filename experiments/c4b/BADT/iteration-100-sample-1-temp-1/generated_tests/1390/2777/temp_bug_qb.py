def original_func(*args):
	global_list = []
	
	(n, x, y) = [int(i) for i in args[0].split()]
	ans = round(((((y / 100) * n) - x) + 0.5))
	if (ans > 0):
	    global_list.append(ans)
	else:
	    global_list.append(0)
	return global_list