def original_func(*args):
	global_list = []
	
	s = args[0]
	count = 0
	ans = 1
	for i in range(1, len(s)):
	    if (count == 4):
	        count = 0
	        ans += 1
	    elif (s[i] == s[(i - 1)]):
	        count += 1
	    if (s[i] != s[(i - 1)]):
	        ans += 1
	        count = 0
	global_list.append(ans)
	return global_list