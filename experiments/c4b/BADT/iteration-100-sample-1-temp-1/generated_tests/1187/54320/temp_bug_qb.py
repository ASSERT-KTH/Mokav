def original_func(*args):
	global_list = []
	
	
	def seperateints(x):
	    k = ''
	    l = []
	    for i in x:
	        if (i == ' '):
	            l.append(int(k))
	            k = ''
	            continue
	        k = (k + i)
	    l.append(int(k))
	    return l
	s = args[0]
	x = s[0].upper()
	kk = (x + s[1:].lower())
	global_list.append(kk)
	return global_list