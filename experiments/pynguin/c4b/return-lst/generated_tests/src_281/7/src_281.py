def func(*args):
	ret_values = []
	
	n = int(args[0])
	A = args[1]
	B = []
	for i in A.split():
	    B.append(int(i))
	if (n == 0):
	    ret_values.append(0)
	else:
	    B.sort(key=None, reverse=True)
	    S = 0
	    x = 0
	    for j in B:
	        S = (S + j)
	        x = (x + 1)
	        if (S >= n):
	            break
	    if (S >= n):
	        ret_values.append(x)
	    else:
	        ret_values.append((- 1))

	return ret_values
