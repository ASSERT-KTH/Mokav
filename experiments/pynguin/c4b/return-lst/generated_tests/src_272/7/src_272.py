def func(*args):
	ret_values = []
	
	(k, r) = args[0].split()
	(k, r) = (int(k), int(r))
	for i in range(1, 1000):
	    a = ((k * i) % 10)
	    if (a == 0):
	        ret_values.append(i)
	        break
	    elif (a == r):
	        ret_values.append(i)
	        break

	return ret_values
