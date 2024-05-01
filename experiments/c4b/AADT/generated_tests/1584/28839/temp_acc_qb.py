def patched_func(*args):
	global_list = []
	
	s = args[0]
	ans = s[0]
	for i in range(1, len(s)):
	    if ((s[(i - 1)] == '/') and (s[i] == '/')):
	        continue
	    ans += s[i]
	if ((ans[(- 1)] == '/') and (len(ans) > 1)):
	    global_list.append(ans[:(- 1)])
	else:
	    global_list.append(ans)
	return global_list