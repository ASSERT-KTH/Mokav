def original_func(*args):
	global_list = []
	
	p = [2]
	n = (int(args[0]) + 1)
	for i in range(3, n):
	    y = 1
	    for j in p:
	        y = (y and (i % j))
	    if y:
	        p += [i]
	global_list.append(sum([(2 == sum([(not (i % j)) for j in p])) for i in range(n)]))
	return global_list