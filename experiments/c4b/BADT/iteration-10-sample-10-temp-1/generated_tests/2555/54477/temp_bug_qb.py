def original_func(*args):
	global_list = []
	
	line = args[0]
	result = 0
	maxi = 1
	for x in range(1, len(line)):
	    if (line[x] == line[(x - 1)]):
	        maxi += 1
	        if (maxi > result):
	            result = maxi
	    else:
	        if (maxi > result):
	            result = maxi
	        maxi = 1
	if (result >= 7):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list