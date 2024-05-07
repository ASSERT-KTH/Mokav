def patched_func(*args):
	global_list = []
	
	str = args[0]
	ar = ['h', 'e', 'l', 'l', 'o']
	i = 0
	for j in str:
	    if (i == len(ar)):
	        break
	    if (j == ar[i]):
	        i += 1
	if (i == len(ar)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list