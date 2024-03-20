def func(*args):
	
	from math import inf
	(m, b) = map(int, args[0].split())
	ans = 0
	for y in range((b + 1)):
	    x = ((b - y) * m)
	    x = int(x)
	    ans = max(ans, (((((x + 1) * y) * (y + 1)) // 2) + ((((y + 1) * x) * (x + 1)) // 2)))
	return(ans)
