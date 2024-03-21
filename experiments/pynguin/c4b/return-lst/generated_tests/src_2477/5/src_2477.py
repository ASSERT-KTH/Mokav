def func(*args):
	ret_values = []
	
	(a, b, n) = list(map(int, args[0].split()))
	a *= 10
	for k in range(10):
	    if (((a + k) % b) == 0):
	        a += k
	        break
	if ((a % b) != 0):
	    ret_values.append((- 1))
	else:
	    ret_values.append((str(a) + ('0' * (n - 1))))

	return ret_values
