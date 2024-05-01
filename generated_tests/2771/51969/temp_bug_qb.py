def original_func(*args):
	global_list = []
	
	(n, t, k, d) = list(map(int, args[0].strip().split(' ')))
	old = 0
	if ((n % k) == 0):
	    old = ((n // k) * t)
	else:
	    old = (((n // k) + 1) * t)
	total = 0
	time1 = 0
	time2 = 0
	while (total < n):
	    if (((time1 % t) == 0) and (time1 > 0)):
	        total += k
	    time1 += 1
	    if ((time2 > d) and (((time2 - d) % t) == 0)):
	        total += k
	    time2 += 1
	if (time1 < old):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list