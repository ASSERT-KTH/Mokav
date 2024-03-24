def func(*args):
	
	n = int(args[0])
	L = args[1]
	cont = 0
	k = 0
	T = ''
	while (k < (n - 1)):
	    if (L[k] == L[(k + 1)]):
	        T += L[k]
	    k += 1
	return(len(T))
