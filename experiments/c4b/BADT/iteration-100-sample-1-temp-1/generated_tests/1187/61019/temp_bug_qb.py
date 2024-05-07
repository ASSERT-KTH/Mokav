def original_func(*args):
	global_list = []
	
	A = str(args[0])
	A = list(A)
	a1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	A1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	
	def Buscar(x):
	    count = (- 1)
	    k = 1
	    while ((k < len(a1)) and (count == (- 1))):
	        if (x == a1[k]):
	            count = 1
	        k += 1
	    return count
	
	def Buscar2(x):
	    count = 0
	    k = 1
	    while ((k < len(a1)) and (count == 0)):
	        if (x == A1[k]):
	            count = 1
	        k += 1
	    return count
	y = 0
	for k in range(len(A)):
	    if (Buscar2(A[k]) == 1):
	        y += 1
	if ((Buscar(A[0]) != (- 1)) and (y == (len(A) - 2))):
	    cadena = ''.join(A)
	    cadena = cadena.capitalize()
	elif (y == len(A)):
	    cadena = ''.join(A)
	    cadena = cadena.lower()
	elif (len(A) == 1):
	    cadena = ''.join(A)
	    cadena = cadena.capitalize()
	else:
	    cadena = ''.join(A)
	global_list.append(cadena)
	return global_list