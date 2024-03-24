def func(*args):
	
	(n, m, z) = map(int, args[0].split(' '))
	ans = 0
	for i in range(1, (z + 1)):
	    if (((i % n) == 0) and ((i % m) == 0)):
	        ans += 1
	return(ans)
