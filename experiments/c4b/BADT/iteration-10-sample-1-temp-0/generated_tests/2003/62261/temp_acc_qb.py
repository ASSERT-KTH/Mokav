def patched_func(*args):
	global_list = []
	
	b = int(args[0])
	while (b < 9500):
	    b = (b + 1)
	    a1 = (b // 1000)
	    a2 = ((b - (a1 * 1000)) // 100)
	    a3 = (((b - (a1 * 1000)) - (a2 * 100)) // 10)
	    a4 = (((b - (a1 * 1000)) - (a2 * 100)) - (a3 * 10))
	    if ((a1 != a2) and (a1 != a3) and (a1 != a4) and (a2 != a3) and (a2 != a4 != a3 != a4)):
	        break
	global_list.append(b)
	return global_list