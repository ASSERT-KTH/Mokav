def func(*args):
	ret_values = []
	
	n = int(args[0])
	k = 1
	mensaje = 'NO'
	while (k < n):
	    r = (n % k)
	    c = (n // k)
	    k = (k + 1)
	    if (r == 0):
	        c = str(c)
	        i = 0
	        x = 0
	        while (i < len(c)):
	            if ((c[i] == '4') or (c[i] == '7')):
	                i = (i + 1)
	                x = (x + 1)
	                if (x == len(c)):
	                    mensaje = 'YES'
	                    k = n
	            else:
	                i = (i + 1)
	ret_values.append(mensaje)

	return ret_values
