def patched_func(*args):
	global_list = []
	
	
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
	    global_list.append('YES')
	else:
	    for i in range(4, int(n)):
	        if islucky(str(i)):
	            if ((int(n) % i) == 0):
	                k += 1
	                break
	    if (k != 0):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list