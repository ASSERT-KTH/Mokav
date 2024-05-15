def original_func(*args):
	global_list = []
	
	k = int(args[0])
	d = [int(a) for a in args[1].split()]
	i = 0
	if (k == 0):
	    global_list.append(0)
	else:
	    while True:
	        a = max(d)
	        k -= a
	        d.remove(a)
	        i += 1
	        if (k <= 0):
	            global_list.append(i)
	            break
	        if (len(d) == 0):
	            break
	return global_list