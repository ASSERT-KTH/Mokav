def patched_func(*args):
	global_list = []
	
	s = args[0]
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	a.sort()
	i = 0
	while (i < (len(a) - 1)):
	    if (a[i] == a[(i + 1)]):
	        a.remove(a[i])
	    else:
	        i += 1
	global_list.append((4 - len(a)))
	return global_list