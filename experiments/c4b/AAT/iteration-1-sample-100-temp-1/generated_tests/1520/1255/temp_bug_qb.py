def original_func(*args):
	global_list = []
	
	(n, a, b, c) = map(int, args[0].split())
	q = []
	
	def f1(k, l):
	    b1 = 0
	    while True:
	        if ((((n - b1) % k) == 0) and ((n - b1) >= 0)):
	            break
	        elif ((n - b1) < 0):
	            b1 -= l
	            break
	        b1 += l
	    if ((((n - b1) % k) == 0) and ((n - b1) >= 0)):
	        return (((n - b1) // k) + (b1 // l))
	    else:
	        return 0
	
	def f2(k, l):
	    b1 = 0
	    while True:
	        if ((((n - b1) % k) == 0) and ((n - b1) >= 0)):
	            break
	        elif ((n - b1) < 0):
	            b1 -= l
	            break
	        b1 += l
	    if ((((n - b1) % k) == 0) and ((n - b1) >= 0)):
	        return (((n - b1) // k) + ((b1 // l) * 2))
	    else:
	        return 0
	q = [f1(a, b), f1(b, c), f1(a, c), f2(a, (b + c)), f2(b, (a + c)), f2(c, (a + b))]
	if ((n % ((a + b) + c)) == 0):
	    q.append(((n // ((a + b) + c)) * 3))
	global_list.append(max(q))
	return global_list