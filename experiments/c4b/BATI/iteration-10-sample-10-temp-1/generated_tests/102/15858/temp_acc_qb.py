def patched_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	d1 = l[0]
	d2 = l[1]
	d3 = l[2]
	r = []
	p1 = ((d1 + d3) + d2)
	r.append(p1)
	p2 = (2 * (d1 + d2))
	r.append(p2)
	p3 = (2 * (d1 + d3))
	r.append(p3)
	p4 = (2 * (d2 + d3))
	r.append(p4)
	r.sort()
	global_list.append(r[0])
	return global_list