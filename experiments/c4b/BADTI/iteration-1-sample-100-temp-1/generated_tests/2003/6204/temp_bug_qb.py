def original_func(*args):
	global_list = []
	
	n = int(args[0])
	for y in range((n + 1), 9000):
	    (d1, d2, d3, d4) = ((y // 1000), ((y // 100) % 10), ((y // 10) % 10), (y % 10))
	    if ((d1 != d2) and (d1 != d3) and (d1 != d4) and (d2 != d3) and (d2 != d4) and (d3 != d4)):
	        global_list.append(y)
	        break
	return global_list