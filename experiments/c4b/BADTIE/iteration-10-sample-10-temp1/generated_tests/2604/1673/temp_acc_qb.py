def patched_func(*args):
	global_list = []
	
	m = args[0]
	n = (str((int(m[0]) - 1)) + ('9' * (len(m) - 1)))
	k = sum(list(map(int, m)))
	p = sum(list(map(int, n)))
	t = l = n
	if (len(m) == 1):
	    t = m
	elif (len(m) > 1):
	    l = ((str((int(n[0]) + 1)) + str((int(n[1]) - 1))) + n[2:])
	    for i in range(1, len(n)):
	        if (int(l) > int(m)):
	            break
	        t = l
	        if (i == (len(n) - 1)):
	            l = (l[0:(- 1)] + str((int(l[(- 1)]) + 1)))
	        else:
	            l = (((l[0:i] + str((int(l[i]) + 1))) + str((int(l[(i + 1)]) - 1))) + l[(i + 2):])
	    if (l <= m):
	        t = l
	global_list.append(int(t))
	return global_list