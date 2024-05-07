def patched_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	(d, p) = (0, 0)
	while (p < c):
	    p += min((v0 + (a * d)), v1)
	    if (d >= 1):
	        p -= l
	    d += 1
	global_list.append(d)
	return global_list