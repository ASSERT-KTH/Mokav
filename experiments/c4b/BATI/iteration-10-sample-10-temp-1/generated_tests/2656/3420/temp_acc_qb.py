def patched_func(*args):
	global_list = []
	
	(n, m) = args[0].split()
	m = int(m)
	k = m
	remove = 0
	n = str(n)
	for i in range((n.__len__() - 1), (- 1), (- 1)):
	    if (k <= 0):
	        break
	    if (n[i] == '0'):
	        k -= 1
	    else:
	        remove += 1
	if (m == k):
	    global_list.append(n.__len__())
	elif (k > 0):
	    global_list.append((n.__len__() - 1))
	else:
	    global_list.append(remove)
	return global_list