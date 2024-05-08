def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	visitedschools = []
	c = 0
	i = 1
	visitedschools += [i]
	j = 1
	while (len(visitedschools) < n):
	    k = ((n + j) - i)
	    j = (2 if (j == 1) else 1)
	    visitedschools += [k]
	    c += ((k + i) % (n + 1))
	global_list.append(c)
	return global_list