def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	if (str(a).replace('4', '').replace('7', '') == ''):
	    global_list.append('YES')
	else:
	    (r, l) = ('0', '0')
	    d = (- 1)
	    h = True
	    while ((int(r) <= a) or (int(l) <= a)):
	        d += 1
	        m = bin(d)[2:]
	        r = m.replace('0', '4').replace('1', '7')
	        l = m.replace('1', '4').replace('0', '7')
	        if (((a % int(r)) == 0) or ((a % int(l)) == 0)):
	            global_list.append('YES')
	            h = False
	            break
	    if h:
	        global_list.append('NO')
	return global_list