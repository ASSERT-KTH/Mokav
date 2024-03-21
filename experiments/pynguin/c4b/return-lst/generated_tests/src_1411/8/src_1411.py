def func(*args):
	ret_values = []
	
	(a, b, n) = map(int, args[0].split())
	a = (a * 10)
	for i in range(0, 10):
	    if (((a + i) % b) == 0):
	        break
	if ((i == 9) and (((a + 9) % b) != 0)):
	    ret_values.append((- 1))
	else:
	    a = (a + i)
	    ret_values.append(a, end='')
	    while (n > 1):
	        ret_values.append(0, end='')
	        n = (n - 1)

	return ret_values
