def func(*args):
	ret_values = []
	
	n = int(args[0])
	c = 0
	for i in range(150000):
	    if ((n % 7) == 0):
	        for k in range(c):
	            ret_values.append(4, end='')
	        for k in range((n // 7)):
	            ret_values.append(7, end='')
	        break
	    n -= 4
	    c += 1
	    if (n < 0):
	        ret_values.append((- 1))
	        break

	return ret_values
