def patched_func(*args):
	global_list = []
	
	l = sorted(list(map(int, args[0].split())))
	p = l[(len(l) // 2)]
	sh = 0
	for i in l:
	    sh += abs((i - p))
	global_list.append(sh)
	return global_list