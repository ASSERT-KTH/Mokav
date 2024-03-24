def func(*args):
	ret_values = []
	
	n = int(args[0])
	ot = '-1'
	ok = 0
	i = ((n // 7) + 1)
	while i:
	    i = (i - 1)
	    o = (n - (7 * i))
	    if ((o % 4) == 0):
	        ot = ''
	        for j in range((o // 4)):
	            ot = (ot + '4')
	        for j in range(i):
	            ot = (ot + '7')
	        ok = 1
	    if ok:
	        break
	ret_values.append(ot)

	return ret_values
