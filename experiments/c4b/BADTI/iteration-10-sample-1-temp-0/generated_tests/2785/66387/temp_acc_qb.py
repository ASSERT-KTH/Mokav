def patched_func(*args):
	global_list = []
	
	s = args[0]
	l = list(s)
	
	def count(l1):
	    a = 0
	    for i in range((len(l1) - 1)):
	        if (l1[i] == 'V'):
	            if (l1[(i + 1)] == 'K'):
	                a = (a + 1)
	    return a
	c = count(list(s))
	b = [c]
	for i in range(len(l)):
	    l1 = l[:]
	    l1[i] = 'V'
	    a = count(l1)
	    b.append(a)
	    l1[i] = 'K'
	    a = count(l1)
	    b.append(a)
	max = c
	for i in range(len(b)):
	    if (b[i] > max):
	        max = b[i]
	global_list.append(max)
	return global_list