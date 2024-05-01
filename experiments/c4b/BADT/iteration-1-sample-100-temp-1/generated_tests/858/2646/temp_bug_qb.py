def original_func(*args):
	global_list = []
	
	(n, a, b, c) = map(int, args[0].split())
	r = (4 - (n % 4))
	aa = []
	aa.append((r * a))
	if (r >= 2):
	    aa.append(((b * (r // 2)) + (a * (r % 2))))
	if (r >= 3):
	    aa.append(((c * (r // 3)) + (a * (r % 3))))
	if (r == 4):
	    global_list.append(0)
	else:
	    global_list.append(min(aa))
	return global_list