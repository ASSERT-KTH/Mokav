def func(*args):
	
	n = int(args[0])
	mid = ((1 + n) // 2)
	return(((mid + n) % (n + 1)))
