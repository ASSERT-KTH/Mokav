def original_func(*args):
	global_list = []
	
	mayus = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
	minus = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	s = args[0]
	ma = 0
	mi = 0
	for c in s:
	    if (c in mayus):
	        ma += 1
	    elif (c in minus):
	        mi += 1
	if (ma > mi):
	    s.upper()
	elif (mi >= ma):
	    s.lower()
	global_list.append(s)
	return global_list