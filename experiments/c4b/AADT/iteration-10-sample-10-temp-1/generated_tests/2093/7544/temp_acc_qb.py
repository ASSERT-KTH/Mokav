def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	if (((k == 1) and (n != 1)) or (k > n)):
	    global_list.append((- 1))
	elif (n == 1):
	    global_list.append('a')
	else:
	    s1 = []
	    s2 = []
	    for i in range((k - 1), 1, (- 1)):
	        c = chr((97 + i))
	        s1.append(c)
	        s2.append(c)
	    for i in range(((n - k) + 2)):
	        if ((i % 2) == 0):
	            s1.append('a')
	            s2.append('b')
	        else:
	            s1.append('b')
	            s2.append('a')
	    s1 = s1[::(- 1)]
	    s2 = s2[::(- 1)]
	    s1 = ''.join(s1)
	    s2 = ''.join(s2)
	    global_list.append(min(s1, s2))
	return global_list