def func(*args):
	
	n = int(args[0])
	s = 'aabb'
	L = (n % 4)
	red = s[0:L]
	time = (n // 4)
	ans = ''
	for _ in range(time):
	    ans += s
	ans += red
	return(ans)
