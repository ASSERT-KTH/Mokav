def original_func(*args):
	global_list = []
	
	s = args[0].strip()
	glas = 'AEIOUY'
	ll = [0]
	j = 0
	for i in range(1, (len(s) + 1)):
	    if (s[(i - 1)] in glas):
	        ll.append((i - j))
	        j = i
	global_list.append(max(ll))
	return global_list