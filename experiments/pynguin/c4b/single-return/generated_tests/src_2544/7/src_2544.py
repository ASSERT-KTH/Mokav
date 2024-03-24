def func(*args):
	
	import sys
	(n, k) = map(int, sys.stdin.readline().split())
	mod_prime = 1000000007
	f = ([0] * (k + 2))
	f[0] = 1
	f[1] = 1
	c = [[1 for j in range((i + 1))] for i in range(k)]
	for i in range(1, len(c)):
	    for j in range(1, (len(c[i]) - 1)):
	        c[i][j] = ((c[(i - 1)][(j - 1)] + c[(i - 1)][j]) % mod_prime)
	for x in range(2, k):
	    f[x] = 0
	    for i in range(0, x):
	        f[x] += ((((c[(x - 1)][i] * f[i]) * f[((x - 1) - i)]) * (i + 1)) % mod_prime)
	ans = (((k * f[(k - 1)]) * ((n - k) ** (n - k))) % mod_prime)
	return(ans)
