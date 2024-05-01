def patched_func(*args):
	global_list = []
	
	s = args[0]
	ans = (- 1)
	if (len(s) > 21):
	    global_list.append((- 1))
	else:
	    n = len(s)
	    for i in range(1, 8):
	        if (i >= n):
	            break
	        m = s[0:i]
	        if (int(m) > 1000000):
	            break
	        if ((m[0] == '0') and (i != 1)):
	            break
	        for j in range(1, 8):
	            if ((i + j) >= n):
	                break
	            mm = s[i:(i + j)]
	            if (int(mm) > 1000000):
	                break
	            if ((mm[0] == '0') and (j != 1)):
	                break
	            mmm = s[(i + j):]
	            if (int(mmm) > 1000000):
	                continue
	            if ((mmm[0] == '0') and (len(mmm) != 1)):
	                continue
	            a = ((int(m) + int(mm)) + int(mmm))
	            if (a > ans):
	                ans = a
	    global_list.append(ans)
	return global_list