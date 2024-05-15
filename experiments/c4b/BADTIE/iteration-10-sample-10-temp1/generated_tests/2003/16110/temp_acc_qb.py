def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	mas = []
	for i in range((a + 1), 15000, 1):
	    r = str(i)
	    r1 = r[0]
	    r2 = r[1]
	    r3 = r[2]
	    r4 = r[3]
	    if ((r1 != r2) and (r1 != r3) and (r1 != r4) and (r2 != r3) and (r2 != r4) and (r3 != r4)):
	        mas.append(r)
	        break
	global_list.append(''.join(mas))
	return global_list