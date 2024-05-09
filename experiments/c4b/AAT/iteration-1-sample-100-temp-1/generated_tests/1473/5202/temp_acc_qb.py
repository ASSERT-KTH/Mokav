def patched_func(*args):
	global_list = []
	
	x = args[0]
	tocke = list(map(int, x.strip().split(' ')))
	(x1, y1, x2, y2, x3, y3) = tocke
	
	def skalarni(v1, v2):
	    return sum(((v1[i] * v2[i]) for i in range(len(v1))))
	
	def right(tocke):
	    (x1, y1, x2, y2, x3, y3) = tocke
	    a = ((x2 - x1), (y2 - y1))
	    b = ((x3 - x1), (y3 - y1))
	    c = ((x3 - x2), (y3 - y2))
	    if (skalarni(a, b) == 0):
	        return True
	    if (skalarni(b, c) == 0):
	        return True
	    if (skalarni(a, c) == 0):
	        return True
	    return False
	
	def legit(tocke):
	    u = set()
	    for k in range(3):
	        dodaj = (tocke[(2 * k)], tocke[((2 * k) + 1)])
	        u.add(dodaj)
	    return (len(u) == 3)
	if right(tocke):
	    global_list.append('RIGHT')
	else:
	    try:
	        for (i, el) in enumerate(tocke):
	            for k in [(- 1), 1]:
	                tocke[i] += k
	                if legit(tocke):
	                    if right(tocke):
	                        global_list.append('ALMOST')
	                        (1 / 0)
	                tocke[i] -= k
	        global_list.append('NEITHER')
	    except:
	        pass
	return global_list