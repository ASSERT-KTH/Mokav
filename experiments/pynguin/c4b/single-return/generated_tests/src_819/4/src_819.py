def func(*args):
	
	n = int(args[0])
	ans = (- 1)
	if ((n % 2) == 1):
	    ans = ((n - 1) // 2)
	else:
	    two = 1
	    while ((two * 2) <= n):
	        two *= 2
	    ans = ((n - two) // 2)
	return(ans)
