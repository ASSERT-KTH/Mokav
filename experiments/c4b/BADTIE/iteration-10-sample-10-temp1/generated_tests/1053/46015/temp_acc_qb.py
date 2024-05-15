def patched_func(*args):
	global_list = []
	
	A = int(args[0])
	ls = []
	lss = []
	i = 0
	m = ''
	k = (A // 7)
	for a in range(k):
	    ls.append(7)
	    lss.append('7')
	l = len(ls)
	while (i < (l + 5)):
	    P = 0
	    for b in ls:
	        P += b
	    if (P == A):
	        global_list.append(m.join(lss))
	        i = 0
	        break
	    else:
	        ls.insert(0, 4)
	        lss.insert(0, '4')
	        if (P > A):
	            del ls[(- 1)]
	            del lss[(- 1)]
	    i += 1
	if (i is not 0):
	    global_list.append((- 1))
	return global_list