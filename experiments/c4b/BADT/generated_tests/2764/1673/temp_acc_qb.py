def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	pp = []
	l = 0
	while (k > 0):
	    if (n == 1):
	        l += 1
	        break
	    for i in range(2, (n + 1)):
	        if (k == 1):
	            pp.append(str(n))
	            k -= 1
	            break
	        elif ((n % i) == 0):
	            k -= 1
	            n = (n // i)
	            pp.append(str(i))
	            break
	global_list.append((' '.join(pp) if (l == 0) else '-1'))
	return global_list