def func(*args):
	
	
	def solve():
	    (n, a, b, c, d) = map(int, args[0].split())
	    ans = 0
	    for i in range(1, (n + 1)):
	        t = ((i + a) + b)
	        if ((((t - a) - c) > 0) and (((t - a) - c) <= n) and (((t - c) - d) > 0) and (((t - c) - d) <= n) and (((t - b) - d) > 0) and (((t - b) - d) <= n)):
	            ans += 1
	    return (ans * n)
	return(solve())
