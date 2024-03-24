def func(*args):
	ret_values = []
	
	
	def seperateints(x):
	    k = ''
	    l = []
	    for i in x:
	        if (i == ' '):
	            l.append(int(k))
	            k = ''
	            continue
	        k = (k + i)
	    l.append(int(k))
	    return l
	x = args[0]
	n = 1
	s = 0
	for i in range(len(x)):
	    if (i == 0):
	        continue
	    elif (x[i] == x[(i - 1)]):
	        n += 1
	    else:
	        n = 1
	    if (n == 7):
	        s += 1
	        ret_values.append('YES')
	        break
	if (s == 0):
	    ret_values.append('NO')

	return ret_values
