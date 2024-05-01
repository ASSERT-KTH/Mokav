def original_func(*args):
	global_list = []
	
	(A, B, n) = map(int, args[0].split())
	if ((A == 0) and (B == 0)):
	    global_list.append(5)
	elif (A == 0):
	    global_list.append('No solution')
	elif (((B / A) % 1) != 0):
	    global_list.append('No solution')
	else:
	    v = (B // A)
	    if (v < 0):
	        x = (- 1)
	    else:
	        x = 1
	    v = pow(abs(v), (1 / n))
	    if (int(v) != v):
	        global_list.append('No solution')
	    else:
	        global_list.append((x * int(v)))
	return global_list