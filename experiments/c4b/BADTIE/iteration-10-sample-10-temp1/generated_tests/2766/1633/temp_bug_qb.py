def original_func(*args):
	global_list = []
	
	string = args[0]
	n = len(string)
	if (n == 1):
	    results = 'YES'
	else:
	    letters = set(string)
	    results = 'NO'
	    for x in range(n):
	        for y in letters:
	            temp = list(string)
	            a = temp[x]
	            temp[x] = y
	            if ((temp[::(- 1)] == temp) and (a != y)):
	                results = 'YES'
	                break
	        if (results == 'YES'):
	            break
	global_list.append(results)
	return global_list