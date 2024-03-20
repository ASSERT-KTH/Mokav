def func(*args):
	
	return(('YES' if any(((c in 'HQ9') for c in args[0])) else 'NO'))
