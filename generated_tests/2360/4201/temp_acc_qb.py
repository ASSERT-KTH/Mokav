def patched_func(*args):
	global_list = []
	
	girl = list(map(int, args[0].split()))
	boy = list(map(int, args[1].split()))
	
	def compatible(b, g):
	    return ((g - 1) <= b <= ((g + 1) * 2))
	if (compatible(boy[0], girl[1]) or compatible(boy[1], girl[0])):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list