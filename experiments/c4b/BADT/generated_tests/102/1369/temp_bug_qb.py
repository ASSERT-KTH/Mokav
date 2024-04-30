def original_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split(' ')))
	a = l[0]
	b = l[1]
	c = l[2]
	one = ((a + b) + c)
	two = (2 * (a + b))
	global_list.append(min(one, two))
	return global_list