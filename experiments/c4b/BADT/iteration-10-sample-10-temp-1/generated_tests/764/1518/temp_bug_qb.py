def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].strip().split(' ')))
	x = 0
	for i in a:
	    x += i
	x = int((x / 3))
	d = 0
	for i in a:
	    d += abs((x - i))
	global_list.append(d)
	return global_list