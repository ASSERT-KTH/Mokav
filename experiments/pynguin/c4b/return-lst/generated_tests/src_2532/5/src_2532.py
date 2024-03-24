def func(*args):
	ret_values = []
	
	
	def DigitosDiferentes(Anio):
	    A = (Anio // 1000)
	    B = ((Anio % 1000) // 100)
	    C = ((Anio % 100) // 10)
	    D = (Anio % 10)
	    L = []
	    L.append(A)
	    L.append(B)
	    L.append(C)
	    L.append(D)
	    L.sort()
	    return (int(L[0]) != int(L[1]) != int(L[2]) != int(L[3]))
	
	def SiguienteAnioDiferente(Anio):
	    i = Anio
	    while (i > 0):
	        i += 1
	        if DigitosDiferentes(i):
	            break
	    return i
	Anio = args[0]
	A = int(Anio)
	ret_values.append(SiguienteAnioDiferente(A))

	return ret_values
