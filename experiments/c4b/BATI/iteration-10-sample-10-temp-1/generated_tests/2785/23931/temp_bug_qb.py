def original_func(*args):
	global_list = []
	
	a = args[0]
	s = 0
	d = []
	d1 = []
	f = 0
	ff = 0
	p = []
	for i in range(len(a)):
	    if ((a[i] == 'V') and (f == 0)):
	        f = (f + 1)
	    elif ((a[i] == 'V') and (f == 1)):
	        f = 1
	        p.append(i)
	        p.append((i - 1))
	    if ((a[i] == 'K') and (f == 1)):
	        f = 0
	        s = (s + 1)
	        d.append(i)
	        d1.append((i - 1))
	    elif ((a[i] == 'K') and (f == 0)):
	        p.append(i)
	for i in range(len(p)):
	    if (a[p[i]] == 'V'):
	        if (((p[i] + 1) not in d1) and ((p[i] - 1) not in d)):
	            s = (s + 1)
	            break
	    if (a[p[i]] == 'K'):
	        if (((p[i] - 1) not in d) and ((p[i] + 1) not in d1)):
	            s = (s + 1)
	            break
	if (len(a) == 1):
	    global_list.append(0)
	else:
	    global_list.append(s)
	return global_list