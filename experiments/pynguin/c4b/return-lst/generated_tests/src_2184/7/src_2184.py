def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = list()
	k = (- 1)
	f = False
	while (n > 0):
	    if (((- k) > len(s)) and ((n % 4) != 0) and f):
	        ret_values.append((- 1))
	        break
	    if ((n >= 7) and (not f)):
	        n -= 7
	        s += ['7']
	    elif ((n % 4) == 0):
	        t = (n // 4)
	        s += (['4'] * t)
	        n = 0
	    elif (len(s) > 0):
	        s[k] = '4'
	        n += 3
	        k -= 1
	        f = True
	    else:
	        f = True
	else:
	    for i in reversed(s):
	        ret_values.append(i, end='')

	return ret_values
