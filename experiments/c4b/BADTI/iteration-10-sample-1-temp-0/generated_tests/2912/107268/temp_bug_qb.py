def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	sum = 1
	for i in range(1, (a + 1)):
	    sum = (i * sum)
	global_list.append(sum)
	return global_list