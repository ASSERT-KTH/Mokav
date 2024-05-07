def original_func(*args):
	global_list = []
	
	n = int(args[0])
	m = n
	a = list(map(int, args[1].split()))
	s = sum(a)
	n = ((n % s) if (n > s) else n)
	r = 0
	for i in range(7):
	    if (n > a[i]):
	        n -= a[i]
	    else:
	        r = i
	        break
	global_list.append((r + 1))
	return global_list