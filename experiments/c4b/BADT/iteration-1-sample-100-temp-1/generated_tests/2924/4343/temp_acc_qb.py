def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	num = str(args[1])
	count = 0
	answer = ''
	for c in num:
	    if (c == '1'):
	        count += 1
	    else:
	        answer += str(count)
	        count = 0
	if (count >= 0):
	    answer += str(count)
	global_list.append(answer)
	return global_list