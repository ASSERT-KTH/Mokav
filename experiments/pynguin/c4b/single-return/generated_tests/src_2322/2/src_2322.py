def func(*args):
	
	C = args[0]
	C = list(C)
	
	def VerCasos(C):
	    if (len(C) == 1):
	        if (C[0].islower() == True):
	            caso = 3
	        else:
	            caso = 4
	    elif (C[0].islower() == True):
	        k = 1
	        while (k < len(C)):
	            if (C[k].isupper() == True):
	                caso = 0
	                k += 1
	            else:
	                caso = 1
	                break
	    elif (C[0].isupper() == True):
	        k = 1
	        while (k < len(C)):
	            if (C[k].isupper() == True):
	                caso = 2
	                k += 1
	            else:
	                caso = 1
	                break
	    return caso
	if (VerCasos(C) == 0):
	    C = ''.join(C)
	    C = C.lower()
	    C = list(C)
	    C[0] = C[0].upper()
	    C = ''.join(C)
	elif (VerCasos(C) == 1):
	    C = ''.join(C)
	elif (VerCasos(C) == 2):
	    C = ''.join(C)
	    C = C.lower()
	elif (VerCasos(C) == 3):
	    C = C[0].upper()
	elif (VerCasos(C) == 4):
	    C = ''.join(C)
	    C = C[0].lower()
	return(C)
