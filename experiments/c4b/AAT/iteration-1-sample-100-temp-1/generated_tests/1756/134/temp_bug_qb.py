def original_func(*args):
	global_list = []
	
	l = [int(x) for x in args[0].split()]
	(a, b, c, d) = map(int, l)
	s = [0 for x in range(4)]
	for e in l:
	    if (e == a):
	        s[0] += 1
	    if (e == b):
	        s[1] += 1
	    if (e == c):
	        s[2] += 1
	    if (e == d):
	        s[3] += 1
	ans = 0
	for e in s:
	    if (e != 1):
	        ans = e
	        break
	global_list.append(((ans - 1) if (ans != 0) else 0))
	return global_list