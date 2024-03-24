def func(*args):
	
	(n, t) = map(int, args[0].split())
	s = args[1]
	for i in range(t):
	    a = list(s)
	    for i in range((n - 1)):
	        if (s[i:(i + 2)] == 'BG'):
	            a[i:(i + 2)] = ['G', 'B']
	    s = ''.join(a)
	return(s)
