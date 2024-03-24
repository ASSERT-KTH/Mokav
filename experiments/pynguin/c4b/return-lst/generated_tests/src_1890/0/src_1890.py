def func(*args):
	ret_values = []
	
	import sys
	(n, k) = args[0].split()
	k = int(k)
	cnt = cnt_zero = no = 0
	if ((len(n) < k) and ('0' in n)):
	    ret_values.append((len(n) - 1))
	else:
	    for i in range((len(n) - 1), (- 1), (- 1)):
	        if (n[i] == '0'):
	            cnt_zero += 1
	        else:
	            if ((i == 0) and (k > cnt_zero)):
	                no = 1
	            if (k > cnt_zero):
	                cnt += 1
	    if (no == 0):
	        ret_values.append(cnt)
	    else:
	        ret_values.append((len(n) - 1))

	return ret_values
