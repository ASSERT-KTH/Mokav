def original_func(*args):
	global_list = []
	
	string = args[0]
	(n, a, b) = string.split()
	a = int(a)
	b = int(b)
	n = int(n)
	front = a
	back = b
	possible_slots = 0
	while (b >= 0):
	    a += 1
	    b -= 1
	    possible_slots += 1
	if (front < back):
	    possible_slots -= 1
	global_list.append(possible_slots)
	return global_list