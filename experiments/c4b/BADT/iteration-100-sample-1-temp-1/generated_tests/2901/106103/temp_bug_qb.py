def original_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	speed = v0
	pages = v0
	days = 1
	while (pages < c):
	    if ((speed + a) <= v1):
	        speed += a
	    pages = ((pages + speed) - l)
	    days += 1
	global_list.append(days)
	return global_list