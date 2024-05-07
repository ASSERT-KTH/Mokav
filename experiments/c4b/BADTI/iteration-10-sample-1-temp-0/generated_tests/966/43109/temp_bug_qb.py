def original_func(*args):
	global_list = []
	
	(n, m, k) = [int(f) for f in args[0].split()]
	(l, r) = (0, m)
	t = True
	for x in range(60):
	    i = ((l + r) // 2)
	    s = ((((((2 * i) - k) * (k - 1)) + ((n - k) * ((((2 * i) - n) + k) - 1))) / 2) + i)
	    if (i == 2):
	        s = (i + (n - 1))
	    if (n == 1):
	        global_list.append(m)
	        t = False
	        break
	    if (s <= m):
	        l = i
	    elif (s >= m):
	        r = i
	if t:
	    global_list.append(l)
	return global_list