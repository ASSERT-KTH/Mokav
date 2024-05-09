def patched_func(*args):
	global_list = []
	
	string = args[0]
	ans = string.count('VK')
	string = string.replace('VK', ' ')
	ans += (1 if (('VV' in string) or ('KK' in string)) else 0)
	global_list.append(ans)
	return global_list