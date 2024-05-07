def original_func(*args):
	global_list = []
	
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0])
	p = 0
	sh = 0
	w = 0
	while True:
	    w += 1
	    p += 6
	    if (p > n):
	        p -= 6
	        global_list.append(l[((((n - p) - 1) // w) % len(l))])
	        break
	return global_list