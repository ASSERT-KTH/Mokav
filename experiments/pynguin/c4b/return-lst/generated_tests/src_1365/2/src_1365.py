def func(*args):
	ret_values = []
	
	from sys import stdin
	(N, K) = map(int, stdin.readline().split())
	
	def check(v):
	    total = 0
	    lines = v
	    while (lines != 0):
	        total += lines
	        lines //= K
	    return (total >= N)
	(l, h) = (0, N)
	while ((h - l) > 1):
	    m = ((l + h) // 2)
	    if check(m):
	        h = m
	    else:
	        l = m
	ret_values.append((l if check(l) else h))

	return ret_values
