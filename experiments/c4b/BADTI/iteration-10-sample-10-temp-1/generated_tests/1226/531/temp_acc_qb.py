def patched_func(*args):
	global_list = []
	
	'input\n433\n109 58 77 10 39 125 15 \n'
	n = int(args[0])
	a = list(map(int, args[1].split()))
	n %= sum(a)
	if (n == 0):
	    n += sum(a)
	s = 0
	for x in range(7):
	    s += a[x]
	    if (s >= n):
	        global_list.append((x + 1))
	        break
	return global_list