def func(*args):
	ret_values = []
	
	
	def Primo(N):
	    div = 0
	    if (N > 1):
	        for k in range(2, N):
	            if ((N % k) == 0):
	                div += 1
	                if (div > 0):
	                    break
	                    return False
	        if (div == 0):
	            return True
	        else:
	            return False
	    else:
	        return False
	
	def CasiPrimo(N):
	    Cont = 0
	    for k in range(2, N):
	        if ((N % k) == 0):
	            if Primo(k):
	                Cont += 1
	                if (Cont > 2):
	                    break
	    if (Cont == 2):
	        return True
	    else:
	        return False
	C = 0
	N = int(args[0])
	for k in range((N + 1)):
	    if CasiPrimo(k):
	        C += 1
	ret_values.append(C)

	return ret_values
