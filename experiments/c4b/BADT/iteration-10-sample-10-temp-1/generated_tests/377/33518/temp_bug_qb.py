def original_func(*args):
	global_list = []
	
	(a1, a2) = [int(x) for x in args[0].split(' ')]
	mins = 0
	while (min(a1, a2) > 0):
	    mins += 1
	    if (a1 == min(a1, a2)):
	        a1 += 1
	        a2 -= 2
	    else:
	        a2 += 1
	        a1 -= 2
	global_list.append(mins)
	return global_list