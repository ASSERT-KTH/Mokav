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
	
	def islucky(x):
	    for i in x:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	n = args[0]
	k = 0
	if islucky(n):
	    ret_values.append('YES')
	else:
	    for i in range(4, int(n)):
	        if islucky(str(i)):
	            if ((int(n) % i) == 0):
	                k += 1
	                break
	    if (k != 0):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
