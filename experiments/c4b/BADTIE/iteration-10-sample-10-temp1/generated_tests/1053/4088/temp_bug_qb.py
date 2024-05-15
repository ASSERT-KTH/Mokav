def original_func(*args):
	global_list = []
	
	n = int(args[0])
	for i in range(((n // 7) + 1)):
	    t = (n - (i * 7))
	    if ((t % 4) == 0):
	        l = ''.join([('7' * i)])
	        ll = ''.join([('4' * (t // 4))])
	        global_list.append(''.join([ll, l]))
	        break
	else:
	    global_list.append((- 1))
	return global_list