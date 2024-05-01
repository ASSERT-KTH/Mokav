def patched_func(*args):
	global_list = []
	
	text = args[0]
	ALF = 'HQ9'
	count = 0
	for ch in text:
	    if (ch in ALF):
	        global_list.append('YES')
	        break
	    else:
	        count += 1
	if (count == len(text)):
	    global_list.append('NO')
	return global_list