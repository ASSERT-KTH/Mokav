def func(*args):
	
	s = list()
	inp = args[0]
	for i in range(len(inp)):
	    s.append(inp)
	    inp = (inp[1:] + inp[0])
	return(len(set(s)))
