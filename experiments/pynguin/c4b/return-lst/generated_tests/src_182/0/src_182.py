def func(*args):
	ret_values = []
	
	p = int(args[0])
	l_n = list(map(int, args[1].split()))
	n_s = sum(l_n)
	while (p > n_s):
	    p -= n_s
	while (p > 0):
	    for i in range(len(l_n)):
	        if (l_n[i] >= p):
	            ret_values.append((i + 1))
	            quit()
	        p -= l_n[i]

	return ret_values
