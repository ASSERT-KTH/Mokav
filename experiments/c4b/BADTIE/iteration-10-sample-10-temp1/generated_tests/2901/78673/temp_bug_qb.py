def original_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = (int(i) for i in args[0].split())
	d = 1
	sum = v0
	while (sum < c):
	    v0 = min(((v0 + (a * d)) - l), (v1 - l))
	    sum = (sum + v0)
	    d = (d + 1)
	global_list.append(d)
	return global_list