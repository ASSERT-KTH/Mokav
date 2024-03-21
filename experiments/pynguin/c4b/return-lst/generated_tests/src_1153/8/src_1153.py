def func(*args):
	ret_values = []
	
	L = args[0]
	L = L.split()
	n = L[0]
	k = int(L[1])
	
	def Div(N, K):
	    N = int(N)
	    if ((N % (10 ** K)) == 0):
	        return True
	    else:
	        return False
	c = 0
	f = len(n)
	while (f != 1):
	    f -= 1
	    if ((n[f] != '0') and (not Div(n, k))):
	        b = (n[:f] + n[(f + 1):])
	        n = b
	        c += 1
	    else:
	        b = n
	if (int(n) == 0):
	    ret_values.append(c)
	else:
	    nd = len(b)
	    nceros = (nd - 1)
	    if (nceros < k):
	        c = (nceros + c)
	    ret_values.append(c)

	return ret_values
