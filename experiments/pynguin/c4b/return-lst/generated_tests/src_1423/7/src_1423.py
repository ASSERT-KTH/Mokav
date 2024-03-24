def func(*args):
	ret_values = []
	
	x = args[0]
	x = x.split()
	N = int(x[0])
	K = int(x[1])
	ceros = 0
	aux = 0
	if (K >= len(x[0])):
	    ret_values.append((len(x[0]) - 1))
	else:
	    while (ceros < K):
	        if ((N % 10) == 0):
	            ceros += 1
	        else:
	            aux += 1
	        N = (N // 10)
	        if (N == 0):
	            ret_values.append((len(x[0]) - 1))
	            ceros = (K + 1)
	    if (ceros <= K):
	        ret_values.append(aux)

	return ret_values
