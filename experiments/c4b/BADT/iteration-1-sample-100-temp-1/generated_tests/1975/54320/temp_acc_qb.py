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
	
	def luckynum(x):
	    for i in x:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	l = seperateints(args[0])
	s = args[1]
	if (len(s) > 1):
	    for i in range(l[1]):
	        kk = ''
	        k = 0
	        while ((k + 1) < len(s)):
	            if ((s[k] == 'B') and (s[(k + 1)] == 'G')):
	                kk = (kk + 'GB')
	                k += 2
	                if ((k + 1) == len(s)):
	                    kk = (kk + s[(len(s) - 1)])
	                    break
	            else:
	                kk = (kk + s[k])
	                if ((k + 1) == (len(s) - 1)):
	                    kk = (kk + s[(k + 1)])
	                k += 1
	        s = kk
	    global_list.append(s)
	else:
	    global_list.append(s)
	return global_list