def func(*args):
	ret_values = []
	
	year = int(args[0])
	found = False
	while (not found):
	    year += 1
	    a = int(divmod(year, 1000)[0])
	    b = divmod(divmod(year, 100)[0], 10)[1]
	    c = divmod(divmod(year, 10)[0], 10)[1]
	    d = int(divmod(year, 10)[1])
	    if ((a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d)):
	        break
	ret_values.append(int(year))

	return ret_values
