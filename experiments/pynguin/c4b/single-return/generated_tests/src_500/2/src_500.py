def func(*args):
	
	(n, a, b) = list(map(int, args[0].split()))
	ans = ((n - max((a + 1), (n - b))) + 1)
	return(ans)
