def original_func(*args):
	global_list = []
	
	inp = args[0].split()
	c = int(inp[0])
	v0 = int(inp[1])
	v1 = int(inp[2])
	a = int(inp[3])
	l = int(inp[4])
	nbpagerest = c
	day = 0
	while (nbpagerest > 0):
	    if (day > 0):
	        nbpagerest = (nbpagerest + l)
	    if ((day * a) <= v1):
	        nbpagerest = ((nbpagerest - v0) - (day * a))
	    else:
	        nbpagerest = (nbpagerest - v1)
	    day = (day + 1)
	global_list.append(day)
	return global_list