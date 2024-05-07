def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = ['I love that ', 'I hate that ']
	d = []
	c = ''
	if ((a % 2) == 0):
	    i = 0
	    while (i < (a - 1)):
	        d.append(b[((i - 1) % 2)])
	        i += 1
	else:
	    i = 0
	    while (i < (a + 1)):
	        d.append(b[((i - 1) % 2)])
	        i += 1
	if ((a % 2) == 1):
	    p = 1
	    while (p < a):
	        c += b[(p % 2)]
	        p += 1
	    global_list.append((c + 'I hate it'))
	else:
	    l = 0
	    while (l < len(d)):
	        c += d[l]
	        l += 1
	    global_list.append((c + 'I love it'))
	return global_list