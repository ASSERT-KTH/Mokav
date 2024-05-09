def original_func(*args):
	global_list = []
	
	s = args[0]
	res = s.count('VK')
	s = s.replace('VK', '')
	res += (('VV' in s) or ('KK' in s))
	global_list.append(res)
	return global_list