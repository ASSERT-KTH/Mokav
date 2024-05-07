def original_func(*args):
	global_list = []
	
	'\nDO NOT ASSUME THAT  K<=L\n'
	k = int(args[0])
	l = int(args[1])
	count = 0
	res = True
	if (k > l):
	    res = False
	while ((l >= k) and res):
	    if ((l % k) != 0):
	        res = False
	        break
	    l //= k
	    count += 1
	if res:
	    global_list.append('YES')
	    global_list.append((count - 1))
	else:
	    global_list.append('NO')
	return global_list