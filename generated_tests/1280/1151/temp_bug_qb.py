def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = list(args[1].split())
	d = {}
	z = 0
	for i in a:
	    i = int(i)
	    if (i > z):
	        z = i
	    d[i] = (d.get(i, 0) + 1)
	f0 = 0
	f1 = d.get(1, 0)
	if (n < 2):
	    global_list.append(f1)
	else:
	    for i in range(2, (z + 1)):
	        s = (f0 + (d.get(i, 0) * i))
	        fi = max(f1, s)
	        f0 = f1
	        f1 = fi
	    global_list.append(f1)
	return global_list