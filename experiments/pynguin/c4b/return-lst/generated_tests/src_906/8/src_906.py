def func(*args):
	ret_values = []
	
	n = args[0]
	n = list(n)
	p = str()
	for i in range(len(n)):
	    h = ord(n[i])
	    if ((64 < h) and (h < 91)):
	        h = (h + 32)
	        if ((h == 97) or (h == 101) or (h == 111) or (h == 105) or (h == 117) or (h == 121)):
	            n[i] = ''
	        else:
	            n[i] = ('.' + chr(h))
	    elif ((h == 97) or (h == 101) or (h == 111) or (h == 105) or (h == 117) or (h == 121)):
	        n[i] = ''
	    else:
	        n[i] = ('.' + chr(h))
	    p += n[i]
	ret_values.append(p)

	return ret_values
