def func(*args):
	ret_values = []
	
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
	    ret_values.append(1)
	else:
	    ret_values.append(0)

	return ret_values
