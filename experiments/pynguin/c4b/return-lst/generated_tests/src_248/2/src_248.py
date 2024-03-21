def func(*args):
	ret_values = []
	
	k = int(args[0])
	months = sorted([int(x) for x in args[1].split(' ')])[::(- 1)]
	days = 0
	m = k
	s = 0
	while (k > 0):
	    if months:
	        k -= months[0]
	        s += months[0]
	        months = months[1:]
	        days += 1
	    else:
	        break
	if (s >= m):
	    ret_values.append(days)
	else:
	    ret_values.append((- 1))

	return ret_values
