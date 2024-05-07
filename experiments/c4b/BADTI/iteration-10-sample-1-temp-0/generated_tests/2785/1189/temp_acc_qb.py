def patched_func(*args):
	global_list = []
	
	s = args[0]
	res = s.count('VK')
	s = s.split('VK')
	res += (sum([(('VV' in x) or ('KK' in x)) for x in s]) > 0)
	global_list.append(res)
	return global_list