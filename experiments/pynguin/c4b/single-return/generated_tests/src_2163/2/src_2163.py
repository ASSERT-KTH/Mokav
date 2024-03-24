def func(*args):
	
	from collections import defaultdict
	(t, k) = (args[0], 0)
	p = defaultdict(list)
	for (j, i) in enumerate(t, 1):
	    p[i].append(j)
	for i in list(p.keys()):
	    if (len(p[i]) < 2):
	        p.pop(i)
	if p:
	    k = 1
	    while True:
	        q = defaultdict(list)
	        for i in p:
	            for j in p[i]:
	                if (j < len(t)):
	                    q[(i + t[j])].append((j + 1))
	        p = q
	        for i in list(p.keys()):
	            if (len(p[i]) < 2):
	                p.pop(i)
	        if (not p):
	            break
	        k += 1
	return(k)
