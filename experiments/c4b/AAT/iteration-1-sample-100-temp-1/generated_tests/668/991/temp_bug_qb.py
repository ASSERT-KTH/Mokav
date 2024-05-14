def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = ['I love that ', 'I hate that ']
	d = []
	c = ''
	i = 1
	while (i < a):
	    d.append(b[((i - 1) % 2)])
	    i += 1
	l = 0
	while (l < len(d)):
	    c += d[((len(d) - 1) - l)]
	    l += 1
	global_list.append(d)
	global_list.append((c + 'I hate it'))
	return global_list