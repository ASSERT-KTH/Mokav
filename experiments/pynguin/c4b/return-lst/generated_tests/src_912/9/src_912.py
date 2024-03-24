def func(*args):
	ret_values = []
	
	
	def floor(x, y):
	    return (x // y)
	
	def ceil(x, y):
	    return ((x // y) + ((x % y) != 0))
	(l, r) = map(int, args[0].split())
	ans = ((l <= 9) * ((min(r, 9) - l) + 1))
	for k in range(0, 17):
	    for d in range(1, 10):
	        rb = (floor((r - d), 10) - ((10 ** k) * d))
	        lb = (ceil((l - d), 10) - ((10 ** k) * d))
	        rx = min(((10 ** k) - 1), rb)
	        lx = max(0, lb)
	        ans += ((rx >= lx) * ((rx - lx) + 1))
	ret_values.append(ans)

	return ret_values
