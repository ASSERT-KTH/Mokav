def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = 'aabbc'
	L = (n % 5)
	red = s[0:L]
	time = (n // 5)
	ans = ''
	for _ in range(time):
	    ans += s
	ans += red
	global_list.append(ans)
	return global_list