def func(*args):
	
	(n, m) = map(int, args[0].split(' '))
	T = args[1]
	for k in range(m):
	    k = 0
	    strq = ''
	    while (k < (n - 1)):
	        if ((T[k] == 'B') and (T[(k + 1)] == 'G')):
	            strq += 'GB'
	            k += 2
	        else:
	            strq += T[k]
	            k += 1
	    if (k == (n - 1)):
	        strq += T[(n - 1)]
	    T = strq
	return(strq)
