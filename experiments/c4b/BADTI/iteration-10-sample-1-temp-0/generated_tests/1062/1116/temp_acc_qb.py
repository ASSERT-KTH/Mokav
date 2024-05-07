def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	K = 0
	while (n > 0):
	    ld = (n % 10)
	    if ((ld == 7) or (ld == 4)):
	        K += 1
	    n = (n // 10)
	if (K > 0):
	    a = 'YES'
	    while ((K > 0) and (a == 'YES')):
	        ld = (K % 10)
	        if ((ld == 7) or (ld == 4)):
	            a = 'YES'
	        else:
	            a = 'NO'
	            break
	        K = (K // 10)
	else:
	    a = 'NO'
	global_list.append(a)
	return global_list