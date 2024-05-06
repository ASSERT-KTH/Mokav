def patched_func(*args):
	global_list = []
	
	a = [int(i) for i in args[0].split()]
	m = int(a[0])
	d = int(a[1])
	if ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
	    if (d <= 5):
	        global_list.append('5')
	    else:
	        global_list.append('6')
	if (m == 2):
	    if (d == 1):
	        global_list.append('4')
	    else:
	        global_list.append('5')
	if ((m == 4) or (m == 6) or (m == 9) or (m == 11)):
	    if (d <= 6):
	        global_list.append('5')
	    else:
	        global_list.append('6')
	return global_list