def original_func(*args):
	global_list = []
	
	n = int(args[0])
	sum = 1
	s = '1'
	while (int(s) <= n):
	    if (int((s + '0')) <= n):
	        sum += 1
	    if (int((s + '1')) <= n):
	        sum += 1
	    s += '0'
	s = '1'
	while (int(s) <= n):
	    if (int((s + '0')) <= n):
	        sum += 1
	    if (int((s + '1')) <= n):
	        sum += 1
	    s += '1'
	if (n == 1):
	    global_list.append(sum)
	elif ((n < 11) and (n > 1)):
	    global_list.append((sum - 1))
	elif (n >= 11):
	    global_list.append((sum - 2))
	return global_list