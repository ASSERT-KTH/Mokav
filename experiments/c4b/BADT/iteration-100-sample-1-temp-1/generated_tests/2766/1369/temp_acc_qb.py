def patched_func(*args):
	global_list = []
	
	import copy
	s = list(args[0])
	a = copy.copy(s)
	a.reverse()
	k = len(s)
	total = 0
	for i in range(0, k):
	    if (s[i] != a[i]):
	        total = (total + 1)
	    if (total > 2):
	        global_list.append('NO')
	        break
	if (total == 2):
	    global_list.append('YES')
	elif ((total == 0) and ((k % 2) == 1)):
	    global_list.append('YES')
	elif (total < 2):
	    global_list.append('NO')
	return global_list