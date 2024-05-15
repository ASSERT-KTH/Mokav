def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = (n // 1234567)
	results = 'NO'
	for x in range(1, (a + 1)):
	    p = (n - (1234567 * x))
	    b = (p // 123456)
	    for y in range(1, (b + 1)):
	        q = (p - (123456 * y))
	        if ((q % 1234) == 0):
	            results = 'YES'
	            break
	    if (results == 'YES'):
	        break
	global_list.append(results)
	return global_list