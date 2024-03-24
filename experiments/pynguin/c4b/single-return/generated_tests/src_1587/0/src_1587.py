def func(*args):
	
	n = int(args[0])
	f1 = 1
	f2 = 1
	ans = (- 1)
	while (f2 <= n):
	    (f1, f2) = (f2, (f1 + f2))
	    ans += 1
	return(ans)
