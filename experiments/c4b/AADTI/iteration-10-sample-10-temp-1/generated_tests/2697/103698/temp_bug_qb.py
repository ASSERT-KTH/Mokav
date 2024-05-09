def original_func(*args):
	global_list = []
	
	(a, b) = (int(i) for i in args[0].split())
	(c, d) = (int(i) for i in args[1].split())
	br = (- 1)
	for k in range(1000000):
	    n = (((d - b) + (c * k)) / a)
	    if ((n >= 0) and (not (n % 1))):
	        br = k
	        global_list.append(br)
	        break
	if (br != (- 1)):
	    global_list.append((d + (c * br)))
	else:
	    global_list.append((- 1))
	return global_list