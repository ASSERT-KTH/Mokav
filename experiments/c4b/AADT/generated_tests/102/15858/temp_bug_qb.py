def original_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	d1 = l[0]
	d2 = l[1]
	d3 = l[2]
	p1 = ((d1 + d3) + d2)
	p2 = (2 * (d1 + d2))
	p3 = (2 * (d1 + d3))
	if ((p1 > p2 >= p3) or (p2 > p1 >= p3)):
	    global_list.append(p3)
	if ((p1 > p3 > p2) or (p3 > p1 > p2)):
	    global_list.append(p2)
	if ((p2 > p3 > p1) or (p3 > p2 >= p1)):
	    global_list.append(p1)
	return global_list