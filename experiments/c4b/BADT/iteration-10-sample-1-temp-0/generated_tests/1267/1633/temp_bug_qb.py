def original_func(*args):
	global_list = []
	
	n = args[0]
	a = (len(n) // 2)
	results = 'NO'
	condition = True
	for x in n:
	    if ((x != '4') and (x != '7')):
	        condition = False
	        break
	if condition:
	    x = sum(map(int, list(n[:a])))
	    y = sum(map(int, list(n[a:])))
	    if (x == y):
	        results = 'YES'
	global_list.append(results)
	return global_list