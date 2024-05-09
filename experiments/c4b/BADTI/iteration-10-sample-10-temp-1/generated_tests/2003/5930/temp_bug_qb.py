def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = 1
	k = (s + n)
	j = 0
	j = (j + k)
	for j in range((n + 1), 9000):
	    l = str(j)
	    if (((l[0] != l[1]) and (l[0] != l[2]) and (l[0] != l[3])) and ((l[1] != l[0]) and (l[1] != l[2]) and (l[1] != l[3])) and ((l[2] != l[0]) and (l[2] != l[1]) and (l[2] != l[3])) and ((l[3] != l[0]) and (l[3] != l[2]) and (l[3] != l[1]))):
	        global_list.append(j)
	        break
	return global_list