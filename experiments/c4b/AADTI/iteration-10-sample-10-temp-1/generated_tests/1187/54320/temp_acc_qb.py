def patched_func(*args):
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
	k = 'S'
	if (len(s) > 1):
	    k = s[1:]
	if k.isupper():
	    kk = ''
	    for i in s:
	        if i.isupper():
	            kk = (kk + i.lower())
	        else:
	            kk = (kk + i.upper())
	    global_list.append(kk)
	else:
	    global_list.append(s)
	return global_list