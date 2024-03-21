def func(*args):
	ret_values = []
	
	(a, b, n) = map(int, args[0].split())
	g = False
	for i in range(10):
	    k = int((str(a) + str(i)))
	    if ((k % b) == 0):
	        g = True
	        break
	if (g == True):
	    final_len = (n + len(str(a)))
	    remaining = (final_len - len(str(k)))
	    ret_values.append((k * (10 ** remaining)))
	else:
	    ret_values.append((- 1))

	return ret_values
