def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range((n // 7), (- 1), (- 1)):
	    t = (n - (i * 7))
	    if ((t % 4) == 0):
	        l = ''.join([('7' * i)])
	        ll = ''.join([('4' * (t // 4))])
	        ret_values.append(''.join([ll, l]))
	        break
	else:
	    ret_values.append((- 1))

	return ret_values
