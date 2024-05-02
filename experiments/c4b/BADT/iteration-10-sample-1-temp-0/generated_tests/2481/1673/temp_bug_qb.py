def original_func(*args):
	global_list = []
	
	n = int(args[0].strip())
	l = 1
	k = 5
	lll = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	while (k <= n):
	    n = (n - k)
	    l += 1
	    k = (2 * k)
	l = (l - 1)
	k = (2 ** l)
	j = 0
	for i in range(5):
	    if (n <= k):
	        global_list.append(lll[j])
	        break
	    else:
	        n = (n - k)
	        j += 1
	return global_list