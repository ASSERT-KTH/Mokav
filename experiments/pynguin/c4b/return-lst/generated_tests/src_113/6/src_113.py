def func(*args):
	ret_values = []
	
	inputs = tuple(map((lambda x: int(x)), args[0].split()))
	n = inputs[0]
	m = inputs[1]
	if (n == 0):
	    ret_values.append(m)
	else:
	    summery = (((1 + n) * n) / 2)
	    last = (m % summery)
	    i = 1
	    while (last >= 0):
	        last -= i
	        i += 1
	    last = int(((last + i) - 1))
	    ret_values.append(last)

	return ret_values
