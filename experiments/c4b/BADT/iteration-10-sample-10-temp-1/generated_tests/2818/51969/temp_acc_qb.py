def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = 'aabb'
	L = (n % 4)
	red = s[0:L]
	time = (n // 4)
	ans = ''
	for _ in range(time):
	    ans += s
	ans += red
	global_list.append(ans)
	return global_list