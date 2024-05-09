def original_func(*args):
	global_list = []
	
	s = args[0]
	v = list(s)
	m = len(v)
	global_list.append(m)
	H = 0
	E = 0
	L = 0
	M = 0
	J = 0
	y = ['q', 'q', 'q', 'q', 'q']
	k = ['h', 'e', 'l', 'l', 'o']
	n = 0
	while (n < m):
	    if (v[n] == 'h'):
	        y[0] = 'h'
	        H = (n + 1)
	        global_list.append('H:', H)
	        break
	    n = (n + 1)
	while (H < m):
	    if (v[H] == 'e'):
	        y[1] = 'e'
	        E = (H + 1)
	        global_list.append('E:', E)
	        break
	    H = (H + 1)
	while (E < m):
	    if (v[E] == 'l'):
	        y[2] = 'l'
	        L = (E + 1)
	        global_list.append('L:', L)
	        break
	    E = (E + 1)
	while (L < m):
	    if (v[L] == 'l'):
	        y[3] = 'l'
	        M = (L + 1)
	        global_list.append('M:', M)
	        break
	    L = (L + 1)
	while (M < m):
	    if (v[M] == 'o'):
	        y[4] = 'o'
	        J = (M + 1)
	        global_list.append('J:', J)
	        break
	    M = (M + 1)
	global_list.append(y)
	if (y == k):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list