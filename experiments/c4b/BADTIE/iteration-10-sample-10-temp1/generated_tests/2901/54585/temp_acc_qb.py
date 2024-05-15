def patched_func(*args):
	global_list = []
	
	(c, v, vm, a, l) = list(map(int, args[0].split()))
	pos = v
	time = 1
	add = v
	while (pos < c):
	    add = min(vm, (add + a))
	    pos += (add - l)
	    time += 1
	global_list.append(time)
	return global_list