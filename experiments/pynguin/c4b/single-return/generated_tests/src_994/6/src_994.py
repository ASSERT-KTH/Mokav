def func(*args):
	
	formt = int(args[0])
	clock = args[1]
	(fn, sn) = clock.split(':')
	if (formt == 24):
	    if (fn > '23'):
	        if (fn[0] > '1'):
	            fn = ('0' + fn[1])
	elif (fn > '12'):
	    if (fn[1] != '0'):
	        if (fn[0] >= '1'):
	            fn = ('0' + fn[1])
	    elif (fn >= '10'):
	        fn = '10'
	elif (fn == '00'):
	    fn = '01'
	if (sn > '59'):
	    if (sn[0] > '5'):
	        sn = ('0' + sn[1])
	return(((fn + ':') + sn), end='')
