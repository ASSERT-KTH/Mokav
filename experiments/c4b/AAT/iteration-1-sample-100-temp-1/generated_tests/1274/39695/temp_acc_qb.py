def patched_func(*args):
	global_list = []
	
	
	def dragons(l):
	    n = l[4]
	    l = sorted(l[:4])
	    for i in range(3):
	        for j in range((i + 1), 4):
	            if ((l[i] != 0) and ((l[j] % l[i]) == 0)):
	                l[j] = 0
	    l = [x for x in l if (x != 0)]
	    r = 0
	    for i in range(1, (n + 1)):
	        for j in range(len(l)):
	            if ((i % l[j]) == 0):
	                r += 1
	                break
	    return r
	k = int(args[0].strip())
	l = int(args[1].strip())
	m = int(args[2].strip())
	n = int(args[3].strip())
	d = int(args[4].strip())
	global_list.append(dragons([k, l, m, n, d]))
	return global_list