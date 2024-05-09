def patched_func(*args):
	global_list = []
	
	s = args[0]
	count = s.count('VK')
	if (('VV' in s.replace('VK', '-')) or ('KK' in s.replace('VK', '-'))):
	    count += 1
	global_list.append(count)
	return global_list