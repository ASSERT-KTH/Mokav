def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = int(args[3])
	e = int(args[4])
	t = [0 for x in range(e)]
	for y in range((a - 1), e, a):
	    t[y] = 1
	for y in range((b - 1), e, b):
	    t[y] = 1
	for y in range((c - 1), e, c):
	    t[y] = 1
	for y in range((d - 1), e, d):
	    t[y] = 1
	ret = 0
	for y in t:
	    if (y == 1):
	        ret += 1
	global_list.append(ret)
	return global_list