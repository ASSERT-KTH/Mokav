def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = 'YES'
	K = 0
	while ((n > 0) and (a == 'YES')):
	    ld = (n % 10)
	    if ((ld == 7) or (ld == 4)):
	        K += 1
	        a = 'YES'
	    else:
	        a = 'NO'
	    n = (n // 10)
	if (a == 'NO'):
	    if (K > 0):
	        a = 'YES'
	        while ((K > 0) and (a == 'YES')):
	            ld = (K % 10)
	            if ((ld == 7) or (ld == 4)):
	                a = 'YES'
	            else:
	                a = 'NO'
	                break
	            K = (K / 10)
	    else:
	        a = 'NO'
	    global_list.append(a)
	else:
	    global_list.append('YES')
	return global_list