def func(*args):
	
	(n, a, b) = map(int, args[0].split())
	ans = (n - a)
	if (ans > (b + 1)):
	    ans = (b + 1)
	return(ans)
