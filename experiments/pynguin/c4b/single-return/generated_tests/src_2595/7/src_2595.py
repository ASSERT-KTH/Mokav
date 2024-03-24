def func(*args):
	
	n = int(args[0])
	ans = ''
	if ((n % 2) != 0):
	    ans += '7'
	    n -= 3
	while (n >= 2):
	    ans += '1'
	    n -= 2
	return(ans)
