def patched_func(*args):
	global_list = []
	
	s = args[0]
	ans = s.count('VK')
	s = s.replace('VK', '--')
	if ((s.find('VV') > (- 1)) or (s.find('KK') > (- 1))):
	    ans += 1
	global_list.append(ans)
	return global_list