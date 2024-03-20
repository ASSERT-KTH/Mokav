def func(*args):
	
	
	def solve(a, b, c):
	    if ((a < 0) or (b < 0) or (c < 0)):
	        return 1e+19
	    if ((a == 0) and (b == 0) and (c == 0)):
	        return 0
	    a = max(a, 0)
	    b = max(b, 0)
	    c = max(c, 0)
	    d = min(a, b, c)
	    a = (a - d)
	    b = (b - d)
	    c = (c - d)
	    arr = [a, b, c]
	    arr.sort()
	    return (arr[1] + ((arr[2] - arr[1]) * 2))
	(a, b, c) = args[0].split(' ')
	a = int(a)
	b = int(b)
	c = int(c)
	ans = 1e+19
	ans = min(ans, solve(a, b, c))
	ans = min(ans, solve(a, (b - 1), c))
	ans = min(ans, solve((a - 1), b, c))
	ans = min(ans, solve(a, b, (c - 1)))
	ans = min(ans, solve((a - 1), (b - 1), c))
	ans = min(ans, solve((a - 1), b, (c - 1)))
	ans = min(ans, solve(a, (b - 1), (c - 1)))
	ans = min(ans, solve((a - 1), (b - 2), (c - 1)))
	return(ans)
