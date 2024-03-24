def func(*args):
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ans = (n // 2)
	else:
	    ans = ((n + 1) // 2)
	return(ans)
