def original_func(*args):
	global_list = []
	
	a = [1 for i in range(26)]
	c = 0
	s = args[0]
	for l in s:
	    if a[(ord(l) - 97)]:
	        c += 1
	        a[(ord(l) - 97)] = 0
	global_list.append(c)
	return global_list