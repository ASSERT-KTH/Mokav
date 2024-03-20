def func(*args):
	
	k = int(args[0])
	r = 0
	for i in range((k - 1)):
	    r += (((k - i) * (i + 1)) - i)
	return((r + 1))
