def original_func(*args):
	global_list = []
	
	(n, a, b, c) = args[0].split(' ')
	n = int(n)
	a = int(a)
	b = int(b)
	c = int(c)
	if ((n % 4) == 0):
	    global_list.append(0)
	else:
	    n = (n % 4)
	    b = (b / 2)
	    c = (c / 3)
	    n = (4 - n)
	    if (n == 3):
	        e = min(a, c)
	        d = int((e * n))
	        global_list.append(int(min(d, (a + (2 * b)))))
	    elif (n == 1):
	        global_list.append(int((a * n)))
	    else:
	        a = min(a, b)
	        global_list.append(int((a * n)))
	return global_list