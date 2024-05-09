def original_func(*args):
	global_list = []
	
	
	def Lucky(x):
	    for i in range(len(x)):
	        if ((x[i] != 4) and (x[i] != 7)):
	            return False
	    return True
	
	def Zelda(A, x):
	    Z = []
	    for i in range(len(A)):
	        if (len(A[i]) == x):
	            Z.append(A[i])
	    return Z
	
	def Combinaciones(a, b, x):
	    A = [a, b]
	    k = 1
	    for i in range((x - 1)):
	        Z = Zelda(A, k)
	        for j in range(len(Z)):
	            A.append((Z[j] + '4'))
	            A.append((Z[j] + '7'))
	        k += 1
	    return A
	
	def Suma(a):
	    r = 0
	    for i in range(len(a)):
	        if ((a[i] == '4') or (a[i] == '7')):
	            r += 1
	    return r
	A = args[0]
	A = Suma(str(A))
	if (A == 0):
	    global_list.append('NO')
	elif Lucky(str(A)):
	    global_list.append('YES')
	else:
	    Z = Combinaciones('4', '7', len(str(A)))
	    A = int(A)
	    k = 0
	    for i in range(len(Z)):
	        if ((A % int(Z[i])) == 0):
	            global_list.append('YES')
	            break
	        k += 1
	    if (k == len(Z)):
	        global_list.append('NO')
	return global_list