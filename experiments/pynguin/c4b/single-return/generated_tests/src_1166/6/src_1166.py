def func(*args):
	
	i = (int(args[0]) + 1)
	while (len(set(str(i))) != 4):
	    i += 1
	return(i)
