def original_func(*args):
	global_list = []
	
	s = args[0]
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	i = 0
	while (i < (len(a) - 1)):
	    j = (i + 1)
	    while (j < len(a)):
	        if (a[i] == a[j]):
	            a.remove(a[j])
	        else:
	            j += 1
	    i += 1
	global_list.append((4 - len(a)))
	return global_list