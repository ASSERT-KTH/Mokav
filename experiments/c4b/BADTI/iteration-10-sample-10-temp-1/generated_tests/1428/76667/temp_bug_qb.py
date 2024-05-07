def original_func(*args):
	global_list = []
	
	a = args[0]
	s = len(a)
	ans = (- 1)
	if (s >= 3):
	    for i in range((s - 2)):
	        for j in range((i + 1), (s - 1)):
	            if ((((i + 1) > (0 + 1)) and (a[0] == '0')) or (((j + 1) > (i + 2)) and (a[(i + 1)] == '0')) or ((s > (j + 2)) and (a[(j + 1)] == '0'))):
	                continue
	            ans = max(ans, ((min(int(a[0:(i + 1)]), int(1000000.0)) + min(int(a[(i + 1):(j + 1)]), int(1000000.0))) + min(int(a[(j + 1):s]), int(1000000.0))))
	global_list.append(ans)
	return global_list