def original_func(*args):
	global_list = []
	
	s = args[0]
	count = 0
	a = []
	a = s.split('VK')
	add = 0
	for i in a:
	    if ((len(i) > 1) and (i != 'KV')):
	        add = 1
	        break
	global_list.append(a)
	global_list.append((s.count('VK') + add))
	return global_list