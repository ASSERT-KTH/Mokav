def original_func(*args):
	global_list = []
	
	(n, t) = map(int, args[0].split())
	s = args[1]
	for i in range(t):
	    a = list(s)
	    for i in range((n - 1)):
	        if (s[i:(i + 1)] == 'BG'):
	            a[i:(i + 1)] = ['G', 'B']
	    s = ''.join(a)
	global_list.append(s)
	return global_list