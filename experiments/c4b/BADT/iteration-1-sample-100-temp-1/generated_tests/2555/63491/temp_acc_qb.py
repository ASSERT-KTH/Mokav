def patched_func(*args):
	global_list = []
	
	b = args[0]
	count = 0
	for i in range((len(b) - 1)):
	    if (b[i] == b[(i + 1)]):
	        count += 1
	    else:
	        count = 0
	    if (count > 5):
	        break
	if (count < 6):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list