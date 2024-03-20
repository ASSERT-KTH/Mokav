def func(*args):
	
	n = int(args[0])
	s = args[1]
	l = [0 for i in range(n)]
	o = 0
	r = 0
	
	def odin(k):
	    j = 0
	    d = False
	    while ((not d) and (j < (len(k) - 1))):
	        d = (k[j] == k[(j + 1)])
	        j += 1
	    return (d, j)
	for i in range(n):
	    l[i] = s[i]
	while odin(l)[0]:
	    del l[odin(l)[1]]
	    o += 1
	return(o)
