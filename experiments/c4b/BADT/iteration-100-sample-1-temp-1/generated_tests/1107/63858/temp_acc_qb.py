def patched_func(*args):
	global_list = []
	
	(simon, antisimon, celkom) = map(int, args[0].split())
	(zobranych, vitaz) = (0, True)
	while (celkom > 0):
	    if vitaz:
	        hrac = simon
	    else:
	        hrac = antisimon
	    for i in range(hrac):
	        if (((hrac % (hrac - i)) == 0) and ((celkom % (hrac - i)) == 0)):
	            zobranych = (hrac - i)
	            break
	    celkom -= zobranych
	    vitaz = (not vitaz)
	if vitaz:
	    global_list.append(1)
	else:
	    global_list.append(0)
	return global_list