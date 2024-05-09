def patched_func(*args):
	global_list = []
	
	
	def Rectangulo(d1, d2, d3):
	    if (((d1 + d2) == d3) or ((d3 + d2) == d1) or ((d1 + d3) == d2)):
	        return True
	    else:
	        return False
	
	def distancia(xa, ya, xb, yb):
	    D = (((xa - xb) ** 2) + ((ya - yb) ** 2))
	    return D
	import math
	L = args[0]
	L = L.split()
	A = []
	xa = int(L[0])
	A.append(xa)
	ya = int(L[1])
	A.append(ya)
	xb = int(L[2])
	A.append(xb)
	yb = int(L[3])
	A.append(yb)
	xc = int(L[4])
	A.append(xc)
	yc = int(L[5])
	A.append(yc)
	d1 = distancia(xa, ya, xb, yb)
	d2 = distancia(xc, yc, xb, yb)
	d3 = distancia(xa, ya, xc, yc)
	if Rectangulo(d1, d2, d3):
	    global_list.append('RIGHT')
	else:
	    Aux = 0
	    for k in range(6):
	        A[k] += 1
	        d1 = distancia(A[0], A[1], A[2], A[3])
	        d2 = distancia(A[4], A[5], A[2], A[3])
	        d3 = distancia(A[0], A[1], A[4], A[5])
	        if ((d1 != d2) and (d2 != d3) and (d3 != 1)):
	            if Rectangulo(d1, d2, d3):
	                Aux = 1
	        A[k] -= 1
	    for k in range(6):
	        A[k] -= 1
	        d1 = distancia(A[0], A[1], A[2], A[3])
	        d2 = distancia(A[4], A[5], A[2], A[3])
	        d3 = distancia(A[0], A[1], A[4], A[5])
	        if ((d1 != d2) and (d2 != d3) and (d3 != 1)):
	            if Rectangulo(d1, d2, d3):
	                Aux = 1
	        A[k] += 1
	    if (Aux == 1):
	        global_list.append('ALMOST')
	    else:
	        global_list.append('NEITHER')
	return global_list