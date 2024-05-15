def original_func(*args):
	global_list = []
	
	s = args[0]
	l = len(s)
	(x, c) = (0, 0)
	for i in range(0, (l - 1)):
	    w = s[i:(i + 2)]
	    if (w == 'VK'):
	        x += 1
	    if ((w == 'VV') or (w == 'KK')):
	        c += 1
	for i in range(0, (l - 2)):
	    w = s[i:(i + 3)]
	    if ((w == 'VKK') or (w == 'KKV') or (w == 'VVK') or (w == 'KVV')):
	        c -= 1
	if (c > 0):
	    x += 1
	global_list.append(x)
	return global_list