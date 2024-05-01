def original_func(*args):
	global_list = []
	
	s = args[0].strip()
	n = len(s)
	big = (10 ** 6)
	result = (- 1)
	for i in range(1, n):
	    if ((s[0] == '0') and (i > 1)):
	        break
	    a = int(s[:i])
	    if (a > big):
	        break
	    for j in range((i + 1), n):
	        if ((s[i] == '0') and ((j - i) > 1)):
	            break
	        b = int(s[i:j])
	        if (b > big):
	            break
	        if ((s[j] == '0') and ((n - j) > 1)):
	            continue
	        c = int(s[j:])
	        if (c > big):
	            break
	        result = max(result, ((a + b) + c))
	global_list.append(result)
	return global_list