def patched_func(*args):
	global_list = []
	
	n = args[0]
	L = 'hello'
	res = 'NO'
	j = 0
	for k in range(len(n)):
	    if (n[k] == L[j]):
	        j += 1
	    if (j == len(L)):
	        res = 'YES'
	        break
	global_list.append(res)
	return global_list