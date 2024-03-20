def func(*args):
	
	n = int(args[0])
	ans = ((n // 3) * 2)
	if ((n % 3) != 0):
	    ans += 1
	return(ans)
