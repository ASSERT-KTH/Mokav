def original_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	(now, day) = (0, 0)
	while (now < c):
	    if (day == 0):
	        now += v0
	    else:
	        now += (v0 - l)
	    if ((v0 + a) <= v1):
	        v0 += a
	    day += 1
	global_list.append(day)
	return global_list