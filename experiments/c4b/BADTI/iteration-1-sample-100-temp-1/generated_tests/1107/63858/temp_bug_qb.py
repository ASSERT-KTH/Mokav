def original_func(*args):
	global_list = []
	
	(simon, antisimon, celkom) = map(int, args[0].split())
	(zobranych, vitaz) = (0, False)
	while (celkom > 0):
	    if vitaz:
	        hrac = simon
	    else:
	        hrac = antisimon
	    for i in range(hrac):
	        if (((simon % (hrac - i)) == 0) and ((celkom % (hrac - i)) == 0)):
	            zobranych = (hrac - i)
	            break
	    celkom -= zobranych
	    vitaz = (not vitaz)
	if vitaz:
	    global_list.append(0)
	else:
	    global_list.append(1)
	return global_list