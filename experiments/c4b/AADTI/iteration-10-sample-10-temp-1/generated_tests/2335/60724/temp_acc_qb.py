def patched_func(*args):
	global_list = []
	
	c = args[0].lower()
	b1 = 'hello'
	p = ('h', 'e', 'l', 'o')
	d = []
	n = ''
	l = 0
	for i in range(0, len(c)):
	    if (c[i] in p):
	        if ((c[i] == 'h') and (c[i] not in d)):
	            d.append(c[i])
	        if ((c[i] == 'e') and ('h' in d) and (c[i] not in d)):
	            d.append(c[i])
	        if ((c[i] == 'l') and ('h' in d) and ('e' in d) and (l < 2)):
	            l = (l + 1)
	            d.append(c[i])
	        if ((c[i] == 'o') and ('h' in d) and ('e' in d) and ('l' in d) and (c[i] not in d) and (l == 2)):
	            d.append(c[i])
	for i in range(0, len(d)):
	    n = (n + d[i])
	if (n == b1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list