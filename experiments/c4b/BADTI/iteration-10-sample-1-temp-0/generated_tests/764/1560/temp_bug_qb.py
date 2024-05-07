def original_func(*args):
	global_list = []
	
	a = args[0]
	b = a.split()
	average = int((((int(b[0]) + int(b[1])) + int(b[2])) / 3))
	dist = ((abs((int(b[0]) - average)) + abs((int(b[1]) - average))) + abs((int(b[2]) - average)))
	global_list.append(dist)
	return global_list