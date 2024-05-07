def original_func(*args):
	global_list = []
	
	year = int(args[0])
	found = False
	while (not found):
	    year += 1
	    a = int(divmod(year, 1000)[0])
	    b = (year / int(divmod(100, 10)[0]))
	    c = (year / int(divmod(10, 10)[0]))
	    d = int(divmod(year, 10)[0])
	    if ((a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d)):
	        break
	global_list.append(int(year))
	return global_list