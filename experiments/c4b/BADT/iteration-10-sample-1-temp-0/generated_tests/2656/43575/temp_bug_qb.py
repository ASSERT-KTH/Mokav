def original_func(*args):
	global_list = []
	
	import sys
	(n, k) = args[0].split()
	k = int(k)
	cnt = cnt_zero = 0
	if ((len(n) < k) and ('0' in n)):
	    global_list.append((len(n) - 1))
	else:
	    for i in range((len(n) - 1), (- 1), (- 1)):
	        if (n[i] == '0'):
	            cnt_zero += 1
	        elif (k > cnt_zero):
	            cnt += 1
	    global_list.append(cnt)
	return global_list