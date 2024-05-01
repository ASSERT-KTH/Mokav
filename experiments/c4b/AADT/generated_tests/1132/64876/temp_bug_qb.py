def original_func(*args):
	global_list = []
	
	a = int(args[0])
	if (str(a).replace('4', '').replace('7', '') == ''):
	    global_list.append('YES')
	else:
	    m = '0'
	    d = (- 1)
	    h = True
	    while (int(m) <= (a ** 0.5)):
	        d += 1
	        m = bin(d)[2:]
	        m = m.replace('0', '4').replace('1', '7')
	        if ((a % int(m)) == 0):
	            global_list.append('YES')
	            h = False
	            break
	    if h:
	        global_list.append('NO')
	return global_list