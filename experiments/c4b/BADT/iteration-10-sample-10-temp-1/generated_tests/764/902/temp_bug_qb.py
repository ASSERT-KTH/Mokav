def original_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	p = (sum(l) // len(l))
	sh = 0
	for i in l:
	    sh += abs((i - p))
	global_list.append(sh)
	return global_list