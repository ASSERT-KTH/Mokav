def patched_func(*args):
	global_list = []
	
	s = args[0]
	c = s.count('VK')
	s = s.replace('VK', 'ms')
	if (('VV' in s) or ('KK' in s)):
	    c += 1
	global_list.append(c)
	return global_list