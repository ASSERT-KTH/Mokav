def original_func(*args):
	global_list = []
	
	n = args[0]
	b = 0
	o = 0
	c = 0
	l = [int(d) for d in str(n)]
	p = len(l)
	for i in range(0, p):
	    if ((l[i] == 4) or (l[i] == 7)):
	        b = (b + 1)
	b = str(b)
	l1 = [int(f) for f in str(b)]
	p1 = len(l1)
	for i in range(0, p1):
	    if ((l[i] == 4) or (l[i] == 7)):
	        c = (c + 1)
	if (c == p1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list