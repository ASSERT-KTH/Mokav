def patched_func(*args):
	global_list = []
	
	n = list(args[0])
	count = 0
	for itch in n:
	    if ((itch == '4') or (itch == '7')):
	        count += 1
	if ((count == 4) or (count == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list