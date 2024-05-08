def patched_func(*args):
	global_list = []
	
	n = args[0]
	m = n.count('VK')
	n = n.replace('VK', 'O')
	if (('VV' in n) or ('KK' in n)):
	    m = (m + 1)
	global_list.append(m)
	return global_list