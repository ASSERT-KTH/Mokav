def original_func(*args):
	global_list = []
	
	
	def f(n, m):
	    res = []
	    for i in range(60):
	        for h in range(60):
	            res.append(((x ** i) + (y ** h)))
	    return list(set(res))
	(x, y, l, r) = map(int, args[0].split(' '))
	unh = f(l, r)
	unh.sort()
	res = 0
	for i in range((len(unh) - 1)):
	    if ((l <= unh[i] <= r) and (l <= unh[(i + 1)] <= r)):
	        res = max(res, (unh[(i + 1)] - unh[i]))
	    elif ((l <= unh[i] <= r) and (unh[(i + 1)] > r)):
	        res = max(res, ((r - unh[i]) + 1))
	    elif ((l > unh[i]) and (l <= unh[(i + 1)] <= r)):
	        res = max(res, ((unh[(i + 1)] - l) + 1))
	if (res != ((10 ** 18) + 1)):
	    global_list.append((res - 1))
	else:
	    global_list.append(0)
	return global_list