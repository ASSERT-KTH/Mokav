def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	(r, l) = map(int, args[1].split())
	if (b == l):
	    global_list.append(a)
	    exit()
	else:
	    L = []
	    for i in range(0, 10000):
	        L.append(((a * i) % r))
	    L1 = []
	    for i in range(0, 10000):
	        L1.append(((r * i) % a))
	    d = (b - l)
	    v = (abs(d) % r)
	    v1 = (abs(d) % a)
	    c = 1
	    if (d > 0):
	        if (v1 in L1):
	            global_list.append(((L1.index(v1) * r) + l))
	            c = 0
	    elif (v in L):
	        global_list.append(((L.index(v) * a) + b))
	        c = 0
	    if (c == 1):
	        global_list.append((- 1))
	return global_list