def func(*args):
	
	s = args[0]
	return(len({(s[i:] + s[:i]) for i in range(len(s))}))
