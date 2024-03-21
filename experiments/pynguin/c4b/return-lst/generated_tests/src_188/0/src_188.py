def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	k = int(k)
	n_z = 0
	d = 0
	for i in range(len(n)):
	    if (n[((len(n) - i) - 1)] == '0'):
	        n_z += 1
	        if (n_z == k):
	            ret_values.append(d)
	            quit()
	    else:
	        d += 1
	ret_values.append((len(n) - 1))

	return ret_values
