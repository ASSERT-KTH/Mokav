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
	
	def luckynum(x):
	    for i in x:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	n = int(args[0])
	i = 5
	while (n > i):
	    n -= i
	    i *= 2
	x = (i / 5)
	nn = 0
	k = 0
	while (k < n):
	    k = (k + x)
	    nn += 1
	if (nn == 1):
	    global_list.append('Sheldon')
	elif (nn == 2):
	    global_list.append('Leonard')
	elif (nn == 3):
	    global_list.append('Penny')
	elif (nn == 4):
	    global_list.append('Rajesh')
	elif (nn == 5):
	    global_list.append('Howard')
	return global_list