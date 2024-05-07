def original_func(*args):
	global_list = []
	
	n = list(map(int, args[0].split()))
	global_list.append(n)
	p = 0
	for a in range(max((n[0] + 1), (n[1] + 1))):
	    for b in range(max((n[0] + 1), (n[1] + 1))):
	        if ((((a * a) + b) == n[0]) and (((b * b) + a) == n[1])):
	            p += 1
	            global_list.append(a, b)
	global_list.append(p)
	return global_list