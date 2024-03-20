def func(*args):
	
	n = int(args[0])
	ans = 0
	if ((n % 2) == 0):
	    ans = (n // 4)
	    if ((n % 4) == 0):
	        ans -= 1
	return(ans)
