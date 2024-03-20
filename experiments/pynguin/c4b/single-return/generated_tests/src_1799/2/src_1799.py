def func(*args):
	
	n = int(args[0])
	mn = ((n // 7) * 2)
	if ((n % 7) == 6):
	    mn += 1
	mx = (2 + (((n - 2) // 7) * 2))
	if (((n - 2) % 7) == 6):
	    mx += 1
	if (n == 1):
	    mn = 0
	    mx = 1
	return(mn, mx)
