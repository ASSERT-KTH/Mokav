def func(*args):
	ret_values = []
	
	
	def Pos(x, A):
	    i = 0
	    while (x != A[i]):
	        i += 1
	    return i
	
	def Lucky(x):
	    for i in range(len(x)):
	        if ((x[i] != '4') and (x[i] != '7')):
	            return False
	    return True
	A = args[0]
	k = 0
	for i in range(len(A)):
	    if ((A[i] == '4') or (A[i] == '7')):
	        k += 1
	if Lucky(str(k)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
