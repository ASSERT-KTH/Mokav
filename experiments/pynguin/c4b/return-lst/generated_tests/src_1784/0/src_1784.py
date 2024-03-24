def func(*args):
	ret_values = []
	
	n = args[0]
	n1 = int(((int(n) ** 0.5) + 1))
	s = 0
	x = int(n)
	n2 = len(n)
	
	def fin(n):
	    l = []
	    for i in range(10):
	        l.append(0)
	    for i in range(10):
	        l[i] = n.count(str(i))
	    return l
	
	def com(a, b):
	    flag = 0
	    for i in range(10):
	        if (b[i] > 0):
	            if (a[i] > 0):
	                flag = 1
	                break
	    if flag:
	        return 1
	    else:
	        return 0
	l = fin(n)
	for i in range(1, n1):
	    if ((x % i) == 0):
	        if (com(fin(str(i)), l) == 1):
	            s += 1
	        if ((x != (i * i)) and (com(fin(str((x // i))), l) == 1)):
	            s += 1
	if (x == 1):
	    ret_values.append(1)
	else:
	    ret_values.append(s)

	return ret_values
