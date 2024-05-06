def original_func(*args):
	global_list = []
	
	s = args[0]
	V = 'V'
	K = 'K'
	res = 0
	flag = False
	d = {'VK': 1, 'VV': 1, 'KK': 1, 'KV': 0}
	if (len(s) < 2):
	    global_list.append(0)
	elif (len(s) == 2):
	    global_list.append(d[s])
	else:
	    for (i, c) in enumerate(list(s)):
	        if (i == 0):
	            continue
	        if ((s[i] == K) and (s[(i - 1)] == V)):
	            res += 1
	        if (i == (len(s) - 1)):
	            continue
	        if (s[i] == s[(i - 1)] == s[(i + 1)]):
	            flag = True
	    global_list.append((res + (1 if flag else 0)))
	return global_list