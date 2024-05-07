def original_func(*args):
	global_list = []
	
	(x, y) = list(map(int, args[0].split()))
	years = 0
	while (x <= y):
	    x *= 3
	    y *= 2
	    if (x > y):
	        break
	    years += 1
	global_list.append(years)
	return global_list