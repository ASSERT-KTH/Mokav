def patched_func(*args):
	global_list = []
	
	(m, d) = args[0].split()
	m = int(m)
	d = int(d)
	c = 0
	if ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
	    c = 5
	    if (d > 5):
	        c = 6
	if (m == 2):
	    c = 4
	    if (d > 1):
	        c = 5
	if ((m == 4) or (m == 6) or (m == 9) or (m == 11)):
	    c = 5
	    if (d == 7):
	        c = 6
	global_list.append(c)
	return global_list