def func(*args):
	
	s = args[0]
	return((s.swapcase() if (s[1:].isupper() or (len(s) == 1)) else s))
