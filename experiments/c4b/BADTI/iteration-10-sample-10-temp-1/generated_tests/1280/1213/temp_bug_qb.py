def original_func(*args):
	global_list = []
	
	n = int(args[0])
	A = args[1]
	B = []
	for i in A.split():
	    B.append(int(i))
	if (n == 0):
	    global_list.append(0)
	else:
	    B.sort(key=None, reverse=True)
	    S = 0
	    x = 0
	    for j in B:
	        S = (S + j)
	        x = (x + 1)
	        if (S >= n):
	            break
	    global_list.append(x)
	return global_list