def original_func(*args):
	global_list = []
	
	n = int(args[0])
	l = list(map(int, args[1].split()))
	i = 0
	j = 0
	k = 0
	while ((k < n) and (j < 7)):
	    k += l[i]
	    j += 1
	    if l[i]:
	        i = j
	global_list.append(i)
	return global_list