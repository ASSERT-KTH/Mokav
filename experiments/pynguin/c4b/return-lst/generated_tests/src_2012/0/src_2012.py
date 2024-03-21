def func(*args):
	ret_values = []
	
	s = list()
	inp = args[0]
	for i in range(len(inp)):
	    s.append(inp)
	    inp = (inp[1:] + inp[0])
	ret_values.append(len(set(s)))

	return ret_values
