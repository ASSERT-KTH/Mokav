def func(*args):
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ans = ((n - 1) // 2)
	else:
	    ans = ((n // 2) - 1)
	return(ans)
