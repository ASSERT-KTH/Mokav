def func(*args):
	
	(a, b) = map(int, args[0].split())
	ans = 0
	while (a <= b):
	    a *= 3
	    b *= 2
	    ans += 1
	return(ans)
