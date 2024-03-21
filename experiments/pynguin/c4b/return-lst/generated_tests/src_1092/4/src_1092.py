def func(*args):
	ret_values = []
	
	k = int(args[0])
	d = [int(a) for a in args[1].split()]
	i = 0
	if (k == 0):
	    ret_values.append(0)
	else:
	    while True:
	        a = max(d)
	        k -= a
	        d.remove(a)
	        i += 1
	        if (k <= 0):
	            ret_values.append(i)
	            break
	        if (len(d) == 0):
	            ret_values.append((- 1))
	            break

	return ret_values
