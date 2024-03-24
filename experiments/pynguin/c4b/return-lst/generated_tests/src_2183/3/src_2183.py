def func(*args):
	ret_values = []
	
	n = int(args[0])
	z = args[1]
	
	def lt(z, n):
	    x = 0
	    m = 0
	    for i in range(n):
	        if ((int(z[i]) != 4) and (int(z[i]) != 7)):
	            return 'NO'
	        if (i < (n // 2)):
	            x = (x + int(z[i]))
	        else:
	            m = (m + int(z[i]))
	    if (m != x):
	        return 'NO'
	    return 'YES'
	ret_values.append(lt(z, n))

	return ret_values
