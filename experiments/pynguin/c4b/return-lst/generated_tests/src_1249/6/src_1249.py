def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	f = 0
	F = []
	for i in range(2, ((n // 2) + 1)):
	    if ((n % i) == 0):
	        while (((n % i) == 0) and (f < (k - 1))):
	            n = (n // i)
	            f = (f + 1)
	            F.append(i)
	        if (f == (k - 1)):
	            break
	if ((f == (k - 1)) and (n != 1)):
	    for i in range(0, len(F)):
	        ret_values.append(F[i], end=' ')
	    ret_values.append(n)
	else:
	    ret_values.append((- 1))

	return ret_values
