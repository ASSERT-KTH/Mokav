def patched_func(*args):
	global_list = []
	
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = (int(args[0]) - 1)
	p = 0
	w = (- 1)
	while True:
	    w += 1
	    p += (5 * (2 ** w))
	    if (p > n):
	        p -= (5 * (2 ** w))
	        k = (n - p)
	        global_list.append(l[(k // (2 ** w))])
	        break
	return global_list