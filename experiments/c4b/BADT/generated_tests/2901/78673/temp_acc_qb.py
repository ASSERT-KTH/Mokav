def patched_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = (int(i) for i in args[0].split())
	d = 1
	sum = v0
	v = 0
	while (sum < c):
	    v = min((v0 + (a * d)), v1)
	    sum = ((sum + v) - l)
	    d = (d + 1)
	global_list.append(d)
	return global_list