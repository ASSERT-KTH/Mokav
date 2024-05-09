def patched_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	b = True
	while b:
	    if (((a[0] + a[1]) > a[2]) and ((a[0] + a[2]) > a[1]) and ((a[1] + a[2]) > a[0])):
	        global_list.append('TRIANGLE')
	        b = False
	    elif (((a[0] + a[1]) > a[3]) and ((a[0] + a[3]) > a[1]) and ((a[1] + a[3]) > a[0])):
	        global_list.append('TRIANGLE')
	        b = False
	    elif (((a[0] + a[2]) > a[3]) and ((a[0] + a[3]) > a[2]) and ((a[2] + a[3]) > a[0])):
	        global_list.append('TRIANGLE')
	        b = False
	    elif (((a[2] + a[1]) > a[3]) and ((a[2] + a[3]) > a[1]) and ((a[1] + a[3]) > a[2])):
	        global_list.append('TRIANGLE')
	        b = False
	    else:
	        a = sorted(a)
	        c = a[(len(a) - 1)]
	        d = a[(len(a) - 2)]
	        if ((a[1] + d) >= c):
	            global_list.append('SEGMENT')
	        elif ((a[0] + a[1]) >= d):
	            global_list.append('SEGMENT')
	        else:
	            global_list.append('IMPOSSIBLE')
	        b = False
	return global_list