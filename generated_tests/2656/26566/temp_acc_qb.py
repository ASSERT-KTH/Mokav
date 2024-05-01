def patched_func(*args):
	global_list = []
	
	a = args[0]
	a = a.split()
	n = int(a[0])
	k = int(a[1])
	m = list(str(n))
	m.reverse()
	res = 0
	cero = 0
	ceros = 0
	for r in m:
	    if (r == '0'):
	        ceros += 1
	if (ceros < k):
	    res = (len(str(n)) - 1)
	else:
	    for j in m:
	        if (j != '0'):
	            res += 1
	        else:
	            cero += 1
	            if (cero == k):
	                break
	global_list.append(res)
	return global_list