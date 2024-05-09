def original_func(*args):
	global_list = []
	
	(n, a, b, c) = list(map(int, args[0].split()))
	D = ([False] * (n + 1))
	D[0] = 0
	for i in range((n + 1)):
	    javobho = []
	    for x in {a, b, c}:
	        try:
	            if (i >= x):
	                javobho.append((D[(i - x)] + 1))
	        except:
	            pass
	    if javobho:
	        D[i] = max(javobho)
	global_list.append(D[(- 1)])
	return global_list