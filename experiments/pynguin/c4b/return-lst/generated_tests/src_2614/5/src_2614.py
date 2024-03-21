def func(*args):
	ret_values = []
	
	(a, b) = (int(i) for i in args[0].split())
	(c, d) = (int(i) for i in args[1].split())
	br = (- 1)
	for k in range(1000000):
	    n = (((d - b) + (c * k)) / a)
	    if ((n >= 0) and (not (n % 1))):
	        br = k
	        break
	if (br != (- 1)):
	    ret_values.append((d + (c * br)))
	else:
	    ret_values.append((- 1))

	return ret_values
