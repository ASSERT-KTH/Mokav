def func(*args):
	ret_values = []
	
	(a, b, n) = map(int, args[0].split())
	flag = False
	a = (a * 10)
	for i in range(0, 10):
	    if (((a + i) % b) == 0):
	        a = (a + i)
	        flag = True
	        break
	if (flag == True):
	    ret_values.append((a * (10 ** (n - 1))))
	else:
	    ret_values.append('-1')

	return ret_values
