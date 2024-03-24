def func(*args):
	ret_values = []
	
	
	def f(n, m):
	    res = []
	    for i in range(60):
	        for h in range(60):
	            res.append(((x ** i) + (y ** h)))
	    res.append((n - 1))
	    res.append((m + 1))
	    return list(set(res))
	(x, y, l, r) = map(int, args[0].split(' '))
	unh = f(l, r)
	unh.sort()
	res = 0
	for i in range((len(unh) - 1)):
	    if (((l - 1) <= unh[i] <= (r + 1)) and ((l - 1) <= unh[(i + 1)] <= (r + 1))):
	        res = max(res, (unh[(i + 1)] - unh[i]))
	ret_values.append((res - 1))

	return ret_values
