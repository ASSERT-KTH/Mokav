def patched_func(*args):
	global_list = []
	
	data = args[0]
	ans = z = 0
	if (len(data) > 1):
	    for (i, f) in enumerate(data):
	        if (i is 0):
	            continue
	        if ((f is 'K') and (data[(i - 1)] is 'V')):
	            ans += 1
	    for (i, f) in enumerate(data):
	        if (i is 0):
	            continue
	        if ((f is 'V') and (data[(i - 1)] is 'V')):
	            if (((i + 1) < len(data)) and (data[(i + 1)] is not 'K')):
	                ans += 1
	                break
	            elif ((i + 1) >= len(data)):
	                ans += 1
	                break
	        elif (f is 'K'):
	            if (data[(i - 1)] is 'V'):
	                continue
	            if ((i > 1) and (data[(i - 2)] is 'K')):
	                ans += 1
	                break
	            elif (i <= 1):
	                ans += 1
	                break
	global_list.append(ans)
	return global_list