def func(*args):
	
	s = args[0]
	a = {(s[i:] + s[:i]) for i in range(len(s))}
	return(len(a))
